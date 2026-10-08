"""Replay the Demo Time act: check every scene, or build the final paper."""

import argparse
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Required, TypedDict, cast

import yaml

DEMO_DIRECTORY = Path(__file__).parent
ACT_FILE = DEMO_DIRECTORY / ".demo" / "paper.yaml"
MAIN_TYP = DEMO_DIRECTORY / "main.typ"
PAPER_PDF = DEMO_DIRECTORY / "paper.pdf"


class Move(TypedDict, total=False):
    action: Required[str]
    position: str
    content: str
    contentPath: str
    startPlaceholder: str
    endPlaceholder: str


class Scene(TypedDict):
    title: str
    moves: list[Move]


class ActError(Exception):
    pass


@dataclass
class SceneFailure:
    title: str
    reason: str


def load_scenes() -> list[Scene]:
    act = cast("dict[str, list[Scene]]", yaml.safe_load(ACT_FILE.read_text()))
    return act["scenes"]


def read_content(move: Move) -> str:
    if "contentPath" in move:
        return (DEMO_DIRECTORY / move["contentPath"]).read_text()
    return move.get("content", "")


def check_placeholders(paper: str, move: Move) -> None:
    start_placeholder = move.get("startPlaceholder")
    if start_placeholder is None:
        raise ActError("only placeholder highlights can be checked")
    start_index = paper.find(start_placeholder)
    if start_index < 0:
        raise ActError(f"start placeholder {start_placeholder!r} not found")
    end_placeholder = move.get("endPlaceholder")
    if end_placeholder is not None and paper.find(end_placeholder, start_index) < 0:
        raise ActError(f"end placeholder {end_placeholder!r} not found")


def apply_move(paper: str, move: Move) -> str:
    match move["action"]:
        case "create":
            return read_content(move)
        case "replace":
            if move.get("position") != "start:end":
                raise ActError("only whole-file replaces (start:end) can be replayed")
            return read_content(move)
        case "insert":
            if move.get("position") != "end":
                raise ActError("only inserts at the end can be replayed")
            # Demo Time overwrites a non-empty target line instead of inserting.
            if paper and not paper.endswith("\n"):
                raise ActError(
                    "the paper must end in a newline before an insert at the end"
                )
            return paper + read_content(move)
        case "highlight":
            check_placeholders(paper, move)
            return paper
        case _:
            return paper


def compile_paper(paper: str, output_path: Path) -> None:
    result = subprocess.run(
        ["typst", "compile", "--root", str(DEMO_DIRECTORY), "-", str(output_path)],
        input=paper,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise ActError(result.stderr)


def check(scenes: list[Scene]) -> int:
    """Compile the paper as it stands after every scene, reporting every failure."""
    failures: list[SceneFailure] = []
    paper = ""
    with tempfile.TemporaryDirectory() as output_directory:
        for scene in scenes:
            try:
                for move in scene["moves"]:
                    paper = apply_move(paper, move)
                compile_paper(paper, Path(output_directory) / "paper.pdf")
            except ActError as error:
                failures.append(SceneFailure(scene["title"], str(error)))

    for failure in failures:
        print(f"Scene {failure.title!r}: {failure.reason}", file=sys.stderr)
    return 1 if failures else 0


def build(scenes: list[Scene]) -> int:
    """Regenerate main.typ from the lesson files and compile it to paper.pdf.

    main.typ is checked in fully assembled, so the live demo has something to reset:
    the Setup scene empties it, and each later scene rebuilds it from lessons/.
    """
    paper = ""
    for scene in scenes:
        for move in scene["moves"]:
            paper = apply_move(paper, move)
    MAIN_TYP.write_text(paper)
    try:
        compile_paper(paper, PAPER_PDF)
    except ActError as error:
        print(error, file=sys.stderr)
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["check", "build"])
    args = parser.parse_args()
    command = cast("Literal['check', 'build']", args.command)
    scenes = load_scenes()
    return check(scenes) if command == "check" else build(scenes)


if __name__ == "__main__":
    sys.exit(main())

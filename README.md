# typst-introduction

A talk that introduces [Typst](https://typst.app), a modern typesetting system and LaTeX alternative.

---

<p align="center">
  <a href="https://ll-nick.github.io/typst-introduction/"><img src="docs/assets/open-button.svg" alt="Open the slides"></a>
</p>

---

The slides double as a standalone reference:
they are meant to be read after the talk, not just watched during it.
Open the presenter view (<kbd>p</kbd> or the button in the status bar)
to see the presenter notes, which contain additional explanations and make the slides self-contained.

## S(l)ide Note

Built with [Inkflow](https://github.com/ll-nick/inkflow),
a presentation tool that assembles slide decks from plain-text sources:
slides drawn in SVG, content in Markdown, and a small Python file tying them together.
It's my own project, take a look if you're curious.

## Development

### Prerequisites

- [mise](https://mise.jdx.dev) (optional but recommended) - installs the toolchain and defines tasks.

or install manually:

- [uv](https://typst.app/docs/guides/for-latex-users/) (for the slides)
- [Typst](https://typst.app) 0.15 (for the demo paper)

### Usage

Run `mise tasks` to list the available tasks (build, paper, check, …).

To preview the slides while editing, run `uv run inkflow serve` or `mise serve`.


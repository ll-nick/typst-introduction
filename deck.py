from inkflow import Deck, Image, MediaFit, Slide, Trigger, animations, transitions


def show_and_hide(id: str, show_at: int) -> list[animations.Animation]:
    return [
        animations.FadeIn(id, Trigger.at(show_at)),
        animations.FadeOut(id, Trigger.at(show_at + 1)),
    ]


def main() -> Deck:
    return Deck(
        transition=transitions.Crossfade(),
        slides=[
            Slide("title", notes="slides/title.md"),
            Slide(
                "tldr",
                md="tldr",
                animations=[
                    *show_and_hide("speed", 1),
                    *show_and_hide("consistent", 2),
                    *show_and_hide("ctan", 3),
                    *show_and_hide("errors", 4),
                ],
            ),
            Slide("content", md="getting-started"),
            # Crash course + live demo
            Slide("section", md="section-crashcourse"),
            Slide("content", md="markup"),
            Slide("content", md="math"),
            Slide("content", md="modes", font_size=34),
            Slide("two-cols", md="types"),
            Slide("content", md="control-flow"),
            Slide("content", md="figures-refs"),
            Slide("content", md="scripting"),
            Slide("content", md="universe"),
            Slide("content", md="templates", font_size=34),
            # kinetic-kit
            Slide(
                "center",
                zones={
                    "content": Image("assets/distracted-me.jpg", fit=MediaFit.CONTAIN)
                },
            ),
            Slide("section", md="section-kinetickit"),
            Slide(
                "kinetic-kit-ksp",
                md="kinetic-kit-ksp",
            ),
            Slide("kinetic-kit-customizable", md="kinetic-kit-customizable"),
            Slide("kinetic-kit-start", md="kinetic-kit-start"),
            Slide("end", md="end"),
        ],
    )

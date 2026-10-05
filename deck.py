from inkflow import Deck, Slide, transitions


def main() -> Deck:
    return Deck(
        transition=transitions.Crossfade(),
        slides=[
            Slide("title", notes="slides/title.md"),
            Slide("two-cols", md="tldr"),
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
            Slide("content", md="templates"),
            # kinetic-kit
            Slide("section", md="section-kinetickit"),
            Slide("content", md="kinetic-kit", font_size=31),
            Slide("end", md="end"),
        ],
    )

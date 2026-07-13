from inkflow import Deck, Slide, transitions


def main() -> Deck:
    return Deck(
        transition=transitions.Crossfade(),
        slides=[
            # 0 · Title & framing
            Slide("cover", md="title", font_size=23),
            # 1 · TL;DR
            Slide("two-cols", md="tldr"),
            # 2 · Getting started
            Slide("default", md="getting-started"),
            # 3 · Crash course + live demo
            Slide("section", md="section-crashcourse"),
            Slide("default", md="markup"),
            Slide("default", md="math"),
            Slide("default", md="scripting"),
            Slide("default", md="figures-refs"),
            Slide("default", md="templates"),
            # 4 · kinetic-kit
            Slide("section", md="section-kinetickit"),
            Slide("default", md="kinetic-kit"),
            # 5 · Wrap-up
            Slide("default", md="wrapup"),
            # 6 · Aside: these slides
            Slide("default", md="inkflow"),
            # Q&A
            Slide("end", md="end"),
        ],
    )

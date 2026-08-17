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
            Slide("content", md="getting-started"),
            # 3 · Crash course + live demo
            Slide("section", md="section-crashcourse"),
            Slide("content", md="markup"),
            Slide("content", md="math"),
            Slide("content", md="scripting"),
            Slide("content", md="figures-refs"),
            Slide("content", md="templates"),
            # 4 · kinetic-kit
            Slide("section", md="section-kinetickit"),
            Slide("content", md="kinetic-kit"),
            # 5 · Wrap-up
            Slide("content", md="wrapup"),
            # 6 · Aside: these slides
            Slide("content", md="inkflow"),
            # Q&A
            Slide("end", md="end"),
        ],
    )

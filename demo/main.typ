#import "@preview/charged-ieee:0.1.4": ieee

#show: ieee.with(
  title: [Just One More Plugin: On the Impact of Perpetual
    Tool Adoption on Dissertation Progress],
  abstract: [
    Doctoral candidates invest substantial effort in optimizing their working environment
    under the hypothesis that a better setup accelerates writing.
    We formalize this behavior through the _tinkering ratio_
    and derive a model predicting time to submission.
    A self-tracked case study supports the model:
    time invested in tooling correlates strongly, and negatively, with pages produced.
    We note — without irony — that this manuscript was migrated
    to a new typesetting system days before the deadline.
  ],
  authors: (
    (
      name: "The Author",
      department: [Institute of Measurement and Control Systems],
      organization: [Karlsruhe Institute of Technology (KIT)],
      location: [Karlsruhe, Germany],
      email: "firstname.lastname@kit.edu",
    ),
  ),
  index-terms: ("procrastination", "tooling", "productivity", "research methods"),
)

= Introduction

Writing a dissertation is *hard*.
Optimizing the _setup_ in which you would write it is,
by comparison, delightful.

Three activities that reliably feel like progress:

- reconfiguring the editor
- evaluating note-taking apps
- migrating to a new typesetting system

This paper asks whether any of them actually help.

= Method

Let $t_"setup"$ and $t_"write"$ be the hours spent tinkering and writing.
We define the _tinkering ratio_

$ r = t_"setup" / (t_"setup" + t_"write") $ <eq:ratio>

Assuming that only $t_"write"$ advances the dissertation,
the time to submission relative to a baseline $T_0$
grows without bound as $r arrow.r 1$:

$ T_"sub" = T_0 / (1 - r) $ <eq:divergence>

= Case Study

#let tinkering(setup, write) = setup / (setup + write)

Self-tracked over one representative month,
the tinkering ratio came to #calc.round(tinkering(68, 3) * 100, digits: 1)% —
not, in hindsight, a sustainable allocation.#footnote[Configuring the time tracker took a weekend.]

= Results

@fig:curve shows the predicted divergence;
@tab:time reports where the month actually went.

#figure(
  image("assets/tinkering-curve.svg", width: 80%),
  caption: [Predicted submission time diverges as the tinkering ratio
    $r arrow.r 1$.],
) <fig:curve>

#let month = (
  (activity: [Rewriting dotfiles], hours: 23, pages: 0),
  (activity: [Implementing a Typst dissertation template], hours: 27, pages: 0.5),
  (activity: [Building a presentation tool], hours: 47, pages: 0),
  (activity: [Actual writing], hours: 3, pages: 1.5),
)

#figure(
  table(
    columns: (1fr, auto, auto),
    align: (left, right, right),
    stroke: none,
    table.hline(),
    table.header([Activity], [Hours], [Pages]),
    table.hline(),
    ..for entry in month {
      (entry.activity, [#entry.hours], [#entry.pages])
    },
    table.hline(),
  ),
  caption: [A representative month.],
) <tab:time>

Of the #month.map(entry => entry.hours).sum() hours logged,
only three went into writing.

= Threats to Validity

The study has a sample size of one @author_inprep,
and that one was — during data collection —
migrating this manuscript to Typst @haug2022
and building a bespoke presentation tool @inkflow.
Time spent on tooling is known to feel like progress @munroe2013,
to expand to fill the schedule @parkinson1955,
and to take longer than any estimate @hofstadter1979.

#bibliography("refs.bib", style: "ieee")

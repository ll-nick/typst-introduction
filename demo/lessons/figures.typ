
= Results

@fig:curve shows the predicted divergence;
@tab:time reports where the month actually went.

#figure(
  image("assets/tinkering-curve.svg", width: 80%),
  caption: [Predicted submission time diverges as the tinkering ratio
    $r arrow.r 1$.],
) <fig:curve>

#let month = (
  (activity: [Rewriting dotfiles], hours: 41, pages: 0),
  (activity: [Migrating LaTeX $arrow.r$ Typst], hours: 27, pages: 0.5),
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

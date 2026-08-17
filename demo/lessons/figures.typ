// Lesson 4 — Figures, tables, and cross-references.

= Results

@fig:curve shows the predicted divergence; @tab:time reports where the month
actually went.

#figure(
  image("../assets/tinkering-curve.svg", width: 80%),
  caption: [Predicted submission time diverges as the tinkering ratio
    $r arrow.r 1$.],
) <fig:curve>

#figure(
  table(
    columns: (1fr, auto, auto),
    align: (left, right, right),
    stroke: none,
    table.hline(),
    table.header([Activity], [Hours], [Pages]),
    table.hline(),
    [Rewriting dotfiles], [14], [0],
    [Migrating LaTeX $arrow.r$ Typst], [11], [0.5],
    [Actual writing], [3], [1.5],
    table.hline(),
  ),
  caption: [A representative month.],
) <tab:time>

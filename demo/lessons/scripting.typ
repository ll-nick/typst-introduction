// Lesson 3 — Scripting: variables, functions, set & show rules.

// A function is just a value — no \newcommand, no fragile macros.
#let tinkering(setup, write) = setup / (setup + write)

// A set rule changes a default for everything that follows.
#set par(justify: true)

Self-tracked over one representative month, the tinkering ratio came to
#calc.round(tinkering(68, 3) * 100, digits: 1)% — not, in hindsight, a
sustainable allocation.

// Reveal (uncomment): a show rule restyles *every* heading at once.
// #show heading: set text(fill: navy)

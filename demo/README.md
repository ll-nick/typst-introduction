# Live demo

Type a concept by hand,
then press the next-scene key:
[Demo Time](https://demotime.show) rebuilds `main.typ` from `lessons/` and highlights the new part.
About 30 minutes.

## Setup

- VS Code with *Tinymist Typst* and *Demo Time*.
- Keybinding (not presentation mode, its <kbd>→</kbd> fires while typing):
  `{ "key": "ctrl+alt+n", "command": "demo-time.start" }`
- `mise run demo-check` checks every scene and caches `charged-ieee`.
- `code demo`, light theme, zoomed in, AI completions and notifications off.
- Reset after a dry run: *Demo Time: Reset*.

## Lessons

### 0 · Start

Run the *Setup* scene (empties and opens `main.typ`),
then *Typst Preview: Preview Opened File*:
an empty file compiles.

### 1 · Markup

```typst
= Introduction

Writing a dissertation is *hard*.

- reconfiguring the editor
+ a numbered item
```

No preamble, instant preview.

### 2 · Math

```typst
= Method

$ r = t_"setup" / (t_"setup" + t_"write") $
```

Spaces make it display math, `/` drops the grouping parentheses, quoted subscripts stay upright.
Show symbol completion.

### 3 · Scripting

```typst
= Case Study

#let tinkering(setup, write) = setup / (setup + write)

The ratio came to #tinkering(68, 3).
```

`#` enters code mode.
Hover for types.
The reveal formats the number with `calc.round`
and adds `#footnote[…]`, a trailing content argument.

### 4 · Figures

```typst
= Results

See @fig:curve.

#figure(image("assets/tinkering-curve.svg"), caption: [Divergence.]) <fig:curve>
```

SVG without conversion, automatic numbering.
The reveal adds a table built by a `for` loop over data
and a total via `.map(…).sum()`.

### 5 · Bibliography

```typst
= Threats to Validity

Tooling feels like progress @munroe2013.

#bibliography("refs.bib")
```

Plain BibTeX, same `@` syntax.
Try `style: "apa"`.

### 6 · Styling

At the top, one line at a time:

```typst
#set page(columns: 2)
#set par(justify: true)
#set heading(numbering: "1.")
#show heading: set text(navy)
#show heading.where(level: 1): it => align(center, it)
```

### 7 · Template

At the very top:

```typst
#import "@preview/charged-ieee:0.1.4": ieee
#show: ieee.with(title: [Just One More Plugin])
```

A template is just a function.
`.with` presets its options; `#show:` hands it the rest of the document.
Navy survives because the own rules come later; the reveal removes them.
Bridge to kinetic-kit.

Afterwards, flip through the crash-course slides as a recap.

## When things go wrong

- Compile error: show it, readable errors are a selling point.
- Demo Time fails: rerun the scene, or paste the lesson file at the end by hand.
- Running late: reveal without typing.

## Editing

`.demo/paper.yaml` lists which lesson files make up each scene and what to highlight.
Lesson paths resolve from `demo/`, since they are pasted into `main.typ`.
`mise run demo-check` replays every scene and compiles the result after each one;
`mise run paper` replays the full act once and builds the final `demo/paper.pdf`.

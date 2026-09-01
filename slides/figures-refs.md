# Figures, references, bibliography

**Figures** — `#figure` numbers and captions; `<label>` and `@ref` tie together.

```typst
See @fig:plot for the trend.

#figure(
  image("plot.svg"),
  caption: [A vector figure.],
) <fig:plot>
```

**Citations** — the same `@` syntax cites a source from a plain BibTeX file.

```typst
Method adapted from @smith2020.
#bibliography("refs.bib")
```

::notes::

`#figure` wraps any content, adds a number and a caption, and makes it
referenceable. The content is arbitrary: it can be an included image, or
something Typst draws itself — a `table`, a chart — and it is numbered either
way.

Images are first-class: `image()` reads SVG, PNG and more directly,
with no package and no Inkscape conversion step.
Labels attach with `<name>` and references use `@name`;
the very same `@key` syntax cites a bibliography entry.
`#bibliography("refs.bib")` reads a plain BibTeX file,
so an existing `.bib` library works unchanged,
and a `style:` argument selects among 80-plus built-in citation styles.

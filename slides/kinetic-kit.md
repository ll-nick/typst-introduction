# Starting a thesis with kinetic-kit

**Start** — from the package (or the web-app gallery), then import it.

```typst
#import "@preview/kinetic-kit:0.1.1": dissertation
```

**Apply** — `dissertation()` for a doctoral thesis, `thesis()` for a Bachelor's/Master's.

```typst
#show: dissertation.with(
  author-firstname: "Max",
  author-surname:   "Mustermann",
  title:            [Reproducible Builds for Robotic Systems],
  lang:             "en",
  abstract-en:      [A short abstract.],
  bibliography:     bibliography("refs.bib", style: "ieee"),
)

= Introduction
```

::notes::

kinetic-kit is the templates idea from the previous slide at full scale. It is a
package on Typst Universe, so `typst init @preview/kinetic-kit:0.1.1` scaffolds a
ready-to-fill project — or you pick it from the template gallery in the web app —
and you apply it with the same everything-`#show` rule as any other template.

It exposes two entry functions: `dissertation(...)` for a doctoral thesis and
`thesis(...)` for a Bachelor's, Master's or Diploma thesis, both bilingual
(`lang: "de"` or `"en"`). A handful of named arguments drive the rest: the
title page, the front matter (abstracts, acknowledgements,
notation and abbreviation lists), the table of contents and lists of figures and
tables, and the back matter (own publications, patents, supervised theses). It
follows the KIT Scientific Publishing rules that a hand-built thesis has to track
by hand — paper formats (`a5`, `17x24`, `a4`), margin presets keyed to the final
page count, binding correction — and ships the KIT color palette and Libertinus
fonts so custom figures match the body. A `bibliography` argument takes an
ordinary `bibliography("refs.bib", style: "ieee")`, and the template supplies the
translated heading. It is MIT-0 licensed.

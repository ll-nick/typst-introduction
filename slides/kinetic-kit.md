# Starting a thesis with kinetic-kit

```typst
#import "@preview/kinetic-kit:0.2.1": thesis

#show: thesis.with(
  lang: "de",
  author-firstname: "Max",
  author-surname: "Mustermann",
  title: [Title of the Dissertation],
  front-matter: [
    #include "content/abstract-de.typ"
    #outline()
  ],
  back-matter: [
    #outline(target: figure.where(kind: image))
    #bibliography("bib/references.bib", style: "ieee")
  ],
)
= Introduction
```

::notes::

kinetic-kit is the templates idea from the previous slide at full scale.
It is a package on Typst Universe,
so `typst init @preview/kinetic-kit:0.2.1` scaffolds a ready-to-fill project —
or you pick it from the template gallery in the web app —
and you apply it with the same everything-`#show` rule as any other template.

A single entry function, `thesis(...)`, covers doctoral theses as well as Bachelor's and Master's theses,
in German or English (`lang: "de"` or `"en"`).
What differs between them is the title page, which is itself a parameter:
the default `doctoral-title-page` is configured with `.with(...)`
(department, advisors, exam date),
and any other content or function can take its place.

Everything else is plain Typst.
Abstracts, acknowledgements and the table of contents are written as ordinary content in `front-matter`,
list pages and the bibliography in `back-matter`, in whatever order the thesis needs.

The `kit-style` export provides the template's fonts, sizes and the KIT color palette,
so custom figures match the body.
It is MIT-0 licensed.

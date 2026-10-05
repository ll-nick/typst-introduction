# Styling *is* programming

**Set** — `#set` changes an element's default from here on.

```typst
#set par(justify: true)
#set heading(numbering: "1.")
```

**Show** — `#show` rewrites how an element renders.

```typst
#show heading: set text(navy)

= A numbered, navy heading
```

::notes::

The same language from earlier — functions, values, control flow — is
what styles the document, through two kinds of rule. A `#set` rule changes an
element's defaults for everything that follows: `set par(justify: true)`
justifies the rest of the document, `set heading(numbering: "1.")` numbers the
headings. A `#show` rule goes further and rewrites how an element is displayed —
`show heading: set text(navy)` recolours every heading at once, and a show rule
can replace an element with arbitrary content of your own.

Together, set and show cover what LaTeX spreads across packages like `titlesec`,
`geometry`, and `fancyhdr`, plus the occasional `\makeatletter`. There is no
separate "preamble language": the document's appearance is written in the very
same language as the document itself.

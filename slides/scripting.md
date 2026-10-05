# Styling *is* programming

**Set** — `#set` changes an element's default from here on.

```typst
#set page(paper: "a4", margin: 2cm)
#set text(font: "New Computer Modern", lang: "en")
#set par(justify: true)
#set heading(numbering: "1.")
```

**Show** — `#show` restyles an element, or replaces it with the result of a function;
without a selector, it applies to everything that follows.

```typst
#show heading: set text(navy)
#show heading.where(level: 1): it => align(center, it)
#show: smallcaps
```

::notes::

The same language from earlier — functions, values, control flow — is what styles the document,
through two kinds of rule.
A `#set` rule changes an element's defaults everywhere in the *current scope*:
`set page(...)` replaces `geometry`,
`set text(...)` picks the font, size and language
(and with it hyphenation and quotes, the job of `babel`),
`set par(justify: true)` justifies the rest of the document,
and `set heading(numbering: "1.")` numbers the headings.

A `#show` rule goes further and rewrites how an element is displayed.
Combined with `set`, it styles one kind of element:
`show heading: set text(navy)` recolours every heading at once.
Given a function instead, it replaces each element with whatever the function returns;
the element is passed in, by convention as `it`,
so `it => align(center, it)` centres it while keeping the default look.
Selectors narrow a rule down, as `heading.where(level: 1)` does here,
and a string or regular expression also works as a selector:
`show "LaTeX": smallcaps` restyles every occurrence of a word.
Leaving out the selector gives the *everything* show rule:
`show: smallcaps` hands the rest of the document to `smallcaps` as a single piece of content,
and is the mechanism behind templates.

# TL;DR: Should you?

## Why you should

::left::

::steps::

Milliseconds, not seconds
: Instant preview, incremental compilation

One coherent language
: Real types & functions
: The same rules everywhere, not new syntax per package

One binary, incl. package manager
: No root, no TeX Live
: Packages fetched & cached on first use

Errors you can read
: Pointed messages, not 200 lines of `\hbox`

::right::

::step::

## Why you shouldn't

Younger ecosystem
: CTAN is much more mature than Typst Universe

::steps::

Younger ecosystem
: Your collaborators are probably still using LaTeX

Younger ecosystem
: You'll probably not get a template for your target conference

::notes::

Why you should:

- **Compile speed.** Typst compiles incrementally, so an edit typically
  re-renders in milliseconds — that is what makes the preview in the web app and
  editor feel instant. LaTeX recompiles the whole document and often needs
  several passes to settle cross-references and citations.
- **One coherent language.** Typst is a complete, well-designed scripting
  language, not a set of macros bolted onto a typesetter. Values have real data
  types — lengths, colors, arrays, dictionaries, functions — and almost
  everything is done by calling functions with the same argument conventions, so
  you learn a handful of general concepts once instead of a different interface
  for every package. Styling follows the same model: a `set` rule changes an
  element's defaults and a `show` rule rewrites how it is displayed. Because the
  rules don't change from one package to the next, common tasks stay consistent
  and predictable rather than each needing its own idioms and escape hatches.
- **One binary, with a package manager.** The compiler is a single
  self-contained binary that needs no root, and it doubles as a package manager:
  packages are downloaded the first time they are used and then cached locally,
  so the install stays small — unlike TeX Live, which can run to several
  gigabytes. Much of what needs a package in LaTeX is built in already: the
  equivalents of amsmath, geometry, hyperref, biblatex, xcolor and graphicx are
  part of the language or its standard library, so a typical document needs no
  preamble at all.
- **Readable errors.** Diagnostics point at a source location with a
  plain-language description, instead of the low-level box and macro errors
  LaTeX often reports.

Why you shouldn't — every entry in this column is really the same point, that
the ecosystem is still young (Typst had its first public release in 2023):

- **Package and template breadth.** CTAN has decades of packages and ready-made
  journal and conference styles; Typst Universe is growing quickly but is far
  smaller, so the template for a specific venue may simply not exist yet. The
  same youth shows in specialised areas like plotting, where LaTeX's TikZ/PGF is
  more mature than Typst's counterpart, CeTZ.
- **Collaborators.** Most colleagues and co-authors still work in LaTeX (or
  Word), so a shared project may not be realistic yet — and there is no
  round-trip conversion to `.docx`.
- **Target venues.** Some conferences and publishers accept only LaTeX source,
  or provide an official template for LaTeX only, which is worth checking before
  committing to Typst for a particular submission.

None of this has to be all-or-nothing: existing BibTeX (`.bib`) libraries work
unchanged, and Pandoc converts existing `.tex` sources into Typst markup — a
conversion also built into the web app.

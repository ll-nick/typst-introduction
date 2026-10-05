# Files, packages & templates

**Files** — `#include` inserts another file's content; `#import` loads its definitions.

```typst
#include "chapters/introduction.typ"
#import "utils.typ": some-helper
```

**Packages** — pulled from Typst Universe as `@preview/name:version`.

```typst
#import "@preview/charged-ieee:0.1.4": ieee
```

**Templates** — just a function; one show rule wraps the whole document.

```typst
#show: ieee.with(
  title: [My Paper Title],
  abstract: [A short abstract.],
)

= Introduction
```

::notes::

A larger document splits into files the same way it would in LaTeX:
`#include` is the counterpart of `\input` and places another file's content where it stands,
while `#import` makes a file's functions and variables available without inserting anything,
so shared definitions live in one place.

A template in Typst is not a mysterious class file —
it is a function that takes your document body and returns a styled version.
You apply it with the *everything* show rule from the styling slide:
`#show: ieee.with(...)` passes everything after it to the `ieee` function.

Packages come from Typst Universe, addressed as `@preview/name:version`.
They download on first use and are cached locally, no need to install anything manually.
`typst init @preview/<template>` scaffolds a new project from one.

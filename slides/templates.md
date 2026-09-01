# Templates & packages

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

A template in Typst is not a mysterious class file — it is a function that takes
your document body and returns a styled version. You apply it with an
*everything* show rule: `#show: ieee.with(...)` passes everything after it to the
`ieee` function.

Packages come from Typst Universe, addressed as `@preview/name:version`.
They download on first use and are cached locally, no need to install anything manually.
`typst init @preview/<template>` scaffolds a new project from one.

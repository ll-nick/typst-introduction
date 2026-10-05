# Typst Universe

**Packages** — one import with a pinned version; downloaded on first use, then cached.

```typst
#import "@preview/cetz:0.5.2"
```

**Equivalents** — most LaTeX staples have a counterpart.

```typst
#(
  tikz:        "cetz",
  beamer:      "touying",
  siunitx:     "unify",
  glossaries:  "glossarium",
  algorithm2e: "lovelace",
  subcaption:  "subpar",
)
```

::notes::

[Typst Universe](https://typst.app/universe) is the package and template registry,
Typst's counterpart to CTAN.
Where the two differ most is how packages reach a document.
A LaTeX package is whatever version the installed TeX distribution ships,
updated for every document at once by `tlmgr` or the next yearly release.
A Typst import names its exact version,
so the document pins its own dependencies:
another machine, a CI job, or the same laptop years later fetches the very same package.
There is no install step and no root access;
the compiler downloads a package the first time it is imported and caches it per user.
Packages are themselves written in Typst,
so their source reads like any other document.

The catalogue is younger and smaller —
about 1,650 packages and templates in October 2026, against CTAN's several thousand —
but the everyday needs of a thesis are covered.
Besides the equivalents above:
`fletcher` draws diagrams with nodes and arrows,
`lilaq` plots data,
`zero` formats numbers like `siunitx`,
`algorithmic` mirrors `algorithmicx`,
`codly` styles code listings,
and `drafting` adds margin notes like `todonotes`.
Packages under development can be installed locally and imported as `@local/name:version`.

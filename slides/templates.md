# Files & templates

**Files** — `#include` inserts another file's content; `#import` loads its definitions.

```typst
#include "chapters/introduction.typ"
#import "utils.typ": some-helper
```

**Presetting arguments** — `.with` returns the function with some arguments filled in.

```typst
#let greet(name, greeting: "Hello") = [#greeting, #name!]
#let welcome = greet.with(greeting: "Welcome")
#welcome("KIT")
```

**Templates** — just a function; `#show:` hands it the rest of the document.

```typst
#import "@preview/charged-ieee:0.1.4": ieee
#show: ieee.with(title: [My Paper Title])
```

::notes::

A larger document splits into files the same way it would in LaTeX:
`#include` is the counterpart of `\input` and places another file's content where it stands,
while `#import` makes a file's functions and variables available without inserting anything,
so shared definitions live in one place.

Every function has a `.with` method.
It does not call the function;
it returns a new one with the given arguments already in place,
and the remaining arguments are supplied when that new function is called.
`welcome("KIT")` is therefore the same as `greet("KIT", greeting: "Welcome")`.

A template in Typst is not a mysterious class file —
it is a function that takes your document body and returns a styled version.
You apply it with the *everything* show rule from the styling slide,
which calls the function with the rest of the document as its only argument.
The template's options have to be filled in before that call,
which is exactly what `.with` does:
`#show: ieee.with(title: …)` presets the title,
and the show rule supplies the body.

Templates are published on Typst Universe like any other package,
and `typst init @preview/<template>` scaffolds a new project from one.

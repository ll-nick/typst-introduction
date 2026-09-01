# A real programming language

**Bindings** — `#let` binds values, functions and closures.

```typst
#let sq(x) = x * x
#let evens = (2, 4, 6)
```

**Control flow** — `#if`, `#for` and `#while` run right in the document.

```typst
#if sq(3) > 5 [big] else [small]
#for e in evens [ #e squared is #sq(e). ]
```

**Methods** — every value carries a standard library.

```typst
#evens.map(sq).filter(x => x > 5)
```

::notes::

Because code mode is a real language, the document can compute itself.
`#let` binds variables and functions (and closures written `x => …`).
`#if`, `#for` and `#while` give ordinary control flow.
Values carry methods — arrays and strings have `.map()`, `.filter()`, `.len()`, `.sorted()`,
alongside library modules like `calc` and `str`.
Anything computed drops back into the document with a leading `#`.

For a LaTeX user this is the largest conceptual jump. Generating a table from a
CSV, numbering something with a loop, or factoring a repeated construct into a
function are a few readable lines here, rather than an expedition into `\loop`,
`\expandafter`, and category codes.

# Values have types

```typst
#(
  content: [a *bold* phrase],
  string:  "hello",
  boolean: true,
  integer: 42,
  float:   3.14,
  length:  12pt,
  ratio:   65%,
)
```

::right::

```typst
#(
  fraction:   1fr,
  angle:      30deg,
  color:      rgb("#1f6feb"),
  array:      (1, 2, 3),
  dictionary: (key: "value"),
  function:   x => x + 1,
)
```

::notes::

Code mode is fully typed, and the set is worth skimming because named arguments
expect specific types. *Content* (`[…]`) is the pivotal one — it holds markup and
is what most functions consume and return. Numbers, strings and booleans behave
as expected.

The layout-specific types are what make Typst expressive: *lengths* (`pt`, `cm`,
`mm`, `in`, `em`), *ratios* (`50%`), and *fractions* (`1fr`, which share out
leftover space the way flexbox does) compose to describe almost any layout;
*angles* and *colors* round out the visual types. *Arrays* and *dictionaries* are
the collections, and *functions* are ordinary values you can store and pass
round.

The examples above are themselves a *dictionary* whose values are one of each
type — the same literal syntax you would write in any code-mode expression.

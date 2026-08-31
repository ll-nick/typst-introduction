# Markup & Code

**Markup** — the default: text, emphasis, lists, no setup.

```typst
Plain *text* with _emphasis_.
```

**Code** — a leading `#` enters it for one expression, then returns to markup.

```typst
Two plus two is #(2 + 2) and this is _content_ again.
```

**Functions** — call with parentheses; the result drops into the text.

```typst
The word #upper("loud") is emphatic.
```

**Content** — the trailing `[…]` is the call's last argument, written *after* the parentheses.

```typst
#link("https://typst.app", [the Typst website]) is the same as
#link("https://typst.app")[the Typst website]
```

::notes::

The markup you saw on the previous slides is *markup mode*, Typst's default. A
leading `#` switches into *code mode* for a single expression — a function call,
a number, a variable — and square brackets `[…]` switch back, letting you nest
markup inside code (and code inside markup) as deeply as you like. That duality
is the one idea the rest of the language builds on.

Code mode is an ordinary expression language, and its most important rule is that
*almost everything is a function call*: `image()`, `text()`, `figure()` — even
the markup shorthands are sugar for functions. Arguments are positional or named
(`link(dest, [label])`), and a trailing content argument can move outside the
parentheses, so `#link("…")[label]` is just `link("…", [label])` written more
conveniently. This is why every styling and figure call in the coming slides
reads the way it does.

# Math

```typst
Inline math like $a^2 + b^2 = c^2$ in a sentence.

A space or newline inside the `$` delimiters switches to a display equation:
$
  sum_(k=1)^n k = (n(n+1)) / 2
$

Symbols (`theta`), accent functions (`hat()`),
shorthands (`->`, `oo`) and quoted text mix freely:
$
  hat(theta)_"MLE" -> theta^* quad "as" n -> oo
$
```

::notes::

Math mode is entered with dollar signs. `$x$` stays inline.
Adding spaces or newlines inside the delimiters — `$ x $` — switches to a centred display equation,
which is why the second equation here is spaced.

Inside math, a single letter is a variable, while multiple letters are read as a symbol name:
`theta`, `sum`, `integral`. Common ones also have shorthands — `->` for `arrow.r`, `oo` for `infinity`.
Accents are function calls — `hat(theta)`, `bar(x)`, `dot(y)` — analogous to `\hat{}` and friends.
A multi-letter identifier is quoted, so a word subscript like `_"MLE"` renders upright text
— the equivalent of LaTeX's `_{\text{MLE}}` — and `"as"` sets ordinary words in an equation.
Delimiters such as parentheses grow to fit their contents automatically.
Most LaTeX math habits carry over; the differences are ergonomic.

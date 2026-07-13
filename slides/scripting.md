# The payoff

## Styling *is* programming

- `#set` — change defaults (font, page, heading numbering)
- `#show` — rewrite how any element renders
- Real functions, variables, loops — no `\def` / `\newcommand` dark arts

::notes::

LIVE: this is the "aha". Re-style the running doc with a few `set` rules
(font, margins, numbered headings). Then a `show` rule to restyle every
figure or every heading at once. Contrast with LaTeX's fragmented styling
(`titlesec`, `geometry`, `fancyhdr`, catcode hacks) — here it's one language.

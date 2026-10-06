# Ready to Publish

::notes::

kinetic-kit is the templates idea from the previous slides at full scale:
a single function, `thesis(...)`, applied with `#show: thesis.with(...)`.

Publishing a dissertation through KIT Scientific Publishing (KSP)
means meeting its layout guidelines:
page format, approved fonts and sizes,
inside margins that grow with the page count, and more.
In the default configuration,
kinetic-kit produces a PDF that follows them,
so the thesis can be submitted without a round of layout fixes.
The repository's `guidelines.md` lists each rule with the code that implements it.

The spread is pages 4 and 5 of the template's full German example.
Everything labelled on it happens without any markup beyond plain headings, figures and references:

- **Running header.**
  Even pages show the current chapter, odd pages the current section.
  The header is left out on chapter-opening pages.
- **Consistent horizontal spacing.**
  Heading numbers sit in a column as wide as the widest number in the document,
  so the titles of all heading levels start at the same position.
- **Consistent vertical spacing.**
  The gaps around headings collapse instead of adding up,
  so a heading followed by text, a subheading or a figure always leaves the same space.
- **Per-chapter numbering.**
  Figures, tables, listings and equations restart in every chapter (*Abbildung 2.1*, *Tabelle 2.1*),
  which Typst does not do on its own. Custom figure types (e.g. algorithms, theorems, ...) are supported, too.
- **Reference labels.**
  A reference to a chapter reads *Kapitel 2*, one to a deeper heading *Abschnitt 2.1*,
  in the document's language.
- **Page numbering.**
  Page numbers sit on the outer edge,
  in Roman numerals for the front matter and Arabic numerals from the first chapter on.
- **Draft marker.**
  `draft: true` prints *ENTWURF* or *DRAFT* on every page,
  optionally with a version string such as the current commit.

KSP endorses only the default configuration of a doctoral thesis,
but the same function produces Bachelor's and Master's theses.

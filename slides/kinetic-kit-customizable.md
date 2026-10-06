# Customizable

**Switches** — common variants, one parameter each.

```typst
#show: thesis.with(
  format: "a4",
  lang: "en",
  margin-preset: "long",
  draft: true,
)
```

**Full control** — your own title page, `kit-style` for matching figures, any package.

::notes::

The images show the same chapter opening in A5 (KSP's recommendation), 17×24 cm and A4,
at their true relative size.
Font sizes and margins follow from `format`.

`lang` (`"de"` or `"en"`) switches hyphenation and quotation marks
as well as every heading and label the template generates,
from *Abbildung 2.1* / *Figure 2.1* to *Literaturverzeichnis* / *Bibliography*.
`draft: true` stamps *ENTWURF* or *DRAFT* on every page;
`draft-info` adds a version string such as the current commit.
Once the thesis is defended,
`doctoral-title-page.with(status-approved: true, exam-date: …)`
switches the title page from the submitted to the approved version.

Beyond the switches, nothing is locked in.
`title-page` accepts any content,
or a function that the template calls with the title, author, format and language;
that is also how a Bachelor's or Master's thesis gets its own title page.
`kit-style` exposes the template's fonts, font sizes and KIT color palette,
so diagrams drawn with `cetz` or `fletcher` match the body text.
Since the thesis is ordinary Typst,
any package from Typst Universe works alongside the template.

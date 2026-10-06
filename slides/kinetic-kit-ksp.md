# Ready to Publish

- Meets KSP's layout guidelines out of the box
- Publish without layout corrections
- Doctoral theses, but also Bachelor's and Master's

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

The spread on the right is pages 4 and 5 of the template's full German example,
with running headers, chapter-wise figure numbering and the draft watermark in the footer.

KSP endorses only the default configuration of a doctoral thesis,
but the same function produces Bachelor's and Master's theses.

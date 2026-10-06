# Where to start

**Start** — from the CLI or the web app.

```bash
typst init @preview/kinetic-kit:0.2.1
```

**Help along the way**

- Examples for every variant
- A cookbook for common extras: glossary, margin notes, custom title page
- A full API reference generated from the source
- Every variant compiled and regression-tested in CI

::notes::

`typst init` copies a commented `main.typ` that already contains every section of a typical thesis,
so the work starts with replacing placeholders rather than reading documentation.

The repository's `examples/` cover doctoral theses in all three formats and both languages,
as well as Master's theses;
each release has them attached as PDFs.
The README's cookbook shows the extras most theses need:
abbreviations with `glossarium`, margin notes with `drafting`,
a custom title page, and short captions for the list of figures with `flex-caption`.
An API reference generated from the source is attached to every release.

The test suite compares rendered pages against reviewed reference images,
so changes to the layout do not go unnoticed.
Because Typst imports pin their version,
a thesis stays on the release it started with until it is upgraded deliberately;
`MIGRATING.md` describes the steps between versions.
The template is MIT-0 licensed.

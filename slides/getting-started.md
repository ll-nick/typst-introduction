# Getting started

## Three ways in

typst.app
: Browser IDE, Overleaf-like — zero install, real-time collaboration, template wizard
: Best for trying it out and co-authoring

Command line
: One small binary — `typst watch paper.typ` recompiles on every save
: Best for local, version-controlled, reproducible builds

Editor + Tinymist
: Language server for VS Code, Neovim, … — live preview, autocomplete, diagnostics
: Best as your daily driver

::step::

*New to it? Start in the browser, go local once you want it in git.*

::notes::

The three on-ramps share the same compiler; they differ only in where you run it.

- **typst.app.** A free web app that works like Overleaf: sign in, create a
  project, and edit in the browser with a live preview and no local install.
  Projects can be shared for real-time collaborative editing, started from a
  template on Typst Universe or the built-in template wizard, and an existing
  `.tex` file can be uploaded and converted to Typst markup (via Pandoc) on the
  way in.
- **Command line.** The compiler is a single self-contained binary — installable
  through the common package managers (Homebrew, winget, Scoop, Cargo, …) or as
  a direct download — that needs no root. `typst compile paper.typ` produces
  `paper.pdf`; `typst watch paper.typ` rebuilds on every save; and
  `typst init @preview/<template>` starts a project from a Universe template.
  Because the sources are plain text and the binary is self-contained, this is
  the on-ramp that fits version control and CI.
- **Editor + Tinymist.** Tinymist is the community language server for Typst. It
  plugs into VS Code (as the "Tinymist Typst" extension), Neovim, Helix, Zed and
  other LSP-capable editors, and adds a live preview, autocomplete for functions
  and symbols, inline error diagnostics, hover documentation and formatting. It
  drives the same local compiler as the command line, so the two go together:
  the CLI builds, Tinymist makes editing comfortable.

A reasonable path for a LaTeX user coming from Overleaf: try things in the web
app, then move to a local editor with Tinymist once you want the document in
version control — the CLI underpins both.

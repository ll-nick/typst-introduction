// Lesson 6 — Templates: one import + one function turns the plain document into
// a full IEEE paper. This is the bridge to kinetic-kit: a template is just a
// function you apply to your content.

#import "@preview/charged-ieee:0.1.4": ieee

// `apply` wraps the accumulated body in the IEEE template. The bibliography
// already lives in the body (lesson 5), so we don't pass one here.
#let apply(body) = ieee.with(
  title: [Just One More Plugin: On the Impact of Perpetual
    Tool Adoption on Dissertation Progress],
  abstract: [
    Doctoral candidates invest substantial effort in optimizing their working
    environment under the hypothesis that a better setup accelerates writing. We
    formalize this behavior through the _tinkering ratio_ and derive a model
    predicting time to submission. A self-tracked case study supports the model:
    time invested in tooling correlates strongly, and negatively, with pages
    produced. We note — without irony — that this manuscript was migrated to a
    new typesetting system days before the deadline.
  ],
  authors: (
    (
      name: "The Author",
      department: [Institute of Measurement and Control Systems],
      organization: [Karlsruhe Institute of Technology (KIT)],
      location: [Karlsruhe, Germany],
      email: "firstname.lastname@kit.edu",
    ),
  ),
  index-terms: ("procrastination", "tooling", "productivity", "research methods"),
)(body)

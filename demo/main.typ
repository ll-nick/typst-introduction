// Live-demo switchboard.
//
// Raise `lesson` to reveal the next step. Each value includes every earlier
// lesson plus the current one, so the paper grows as you count up. The final
// lesson wraps the whole thing in a real IEEE template.
//
//   1 markup   2 math   3 scripting   4 figures   5 bibliography   6 template

#let lesson = 6

#let body = {
  include "lessons/markup.typ"
  if lesson >= 2 { include "lessons/math.typ" }
  if lesson >= 3 { include "lessons/scripting.typ" }
  if lesson >= 4 { include "lessons/figures.typ" }
  if lesson >= 5 { include "lessons/bibliography.typ" }
}

#if lesson >= 6 {
  import "lessons/template.typ": apply
  apply(body)
} else {
  body
}

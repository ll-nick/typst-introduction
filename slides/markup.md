# Markup basics

```typst
= Heading
== Subheading

Text with *bold* and _italic_ words.

- a bullet
- another bullet
+ a numbered item
```

::notes::

Typst starts in *markup mode*: text is just text, and a blank line is a
paragraph break.
The most common elements get special syntax, so a simple document reads similar to Markdown.
A leading `=` marks a heading (`==` a subheading, and so on),
`*stars*` give bold, `_underscores_` italics, and a line beginning with `-`
(or `+` for numbered) is a list item.

There is no document class to choose and no `\begin{document}`.
An empty file produces a valid PDF with sane defaults.

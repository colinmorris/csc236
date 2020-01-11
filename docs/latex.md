# LaTeX

LaTeX is a system in which you write some code which is used as a recipe to generate a nice-looking document - in this sense, it bears some similarity to HTML, or Markdown. It is the standard for academic writing in math and computer science. If this is your first experience with LaTeX, you may find it initially challenging, and even frustrating, but you will find it to be an essential skill if you plan to take more theory courses in the future, or if you plan to write academic papers for publication.

## Compiling LaTeX

There are two good options for turning a `.tex` source file into a pdf. 

### On the command line

```
$ pdflatex a1.tex
```

This will generate a lot of incomprehensible output, but when it's done, you should have a file `a1.pdf` in the current directory. (Or, if you're unlucky, an error message.)

I recommend using CDF for this. If you want to use your own machine, you will need to install `pdflatex`, and possibly also some extra LaTeX packages. (Install steps will vary depending on your operating system.)

### Overleaf

Another convenient (and possibly more beginner-friendly) approach is to compile your LaTeX in "the cloud" using [Overleaf](http://overleaf.com/).

David Liu has a [good introductory video](https://www.youtube.com/watch?v=j7HsaFSKNGQ) about Overleaf from 2014 (back when it was known as ShareLaTeX). The interface has changed slightly since then, but most of the information is still relevant.

## Example files

A good starting point for assignments is the starter code (e.g. [a1_starter.tex](assignments/a1_starter.tex)). It includes, among other things, the LaTeX source that was used to generate the questions as they appear on the assignment handout. It also comes with a lot of comments (the lines beginning with '%') explaining what's going on.

You may also wish to take a look at the file [example_proof.tex](misc/example_proof.tex). This has an example of an inductive proof written up using some of the helpers included in the a1 starter code. However, you're not required to hew to the formatting used in that document - there are many different, reasonable ways to format the same proof.

The document [sample_latex.tex](https://www.cs.toronto.edu/~david/courses/csc236_w14/resources/sample_latex.tex), written by David Liu (and shown in the video linked above), gives a great introduction to many of LaTeX's features, over the course of several pages. It also requires the package file [ut-csc.sty](https://www.cs.toronto.edu/~david/courses/csc236_w14/resources/ut-csc.sty) to compile.

## Other useful links

* [The Not So Short Introduction to LaTeX](http://ctan.mirror.rafal.ca/info/lshort/english/lshort.pdf)
* [Wikibooks: LaTeX](https://en.wikibooks.org/wiki/LaTeX) 

## Getting help

You can ask questions about LaTeX on the course discussion board, using the 'latex' tag.

I'm also happy to try to answer LaTeX questions or help debug LaTeX issues during office hours.

If there is enough interest, I may schedule some extra office hours dedicated to LaTeX help before the first assignment due date (likely early in week 3).

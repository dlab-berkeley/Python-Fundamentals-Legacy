# Python Basics: 0-1 Introduction.

This unit provides a basic introduction to Python. By the end of the week, you should be able to:

1. Run Python from both the Shell and in an IPython Notebook
2. Write basic commands using Python syntax
3. Grasp the major Python [object](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#object) [types](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#type), including [integers](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#integer), [floats](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#floating-point-number), [strings](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#string), lists, sets, and dictionaries
4. Operate and manipulate those objects
5. Integrate choices into your programs using [conditionals](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#conditional-statement)


# What is Programming

> ## Learning Objectives
>
> *   Explain the difference between knowing a programming language and knowing how to program.
> *   Explain how programming languages can differ.
> *   Give useful debugging tips.
> *   Offer helpful resource websites.
> *   Explain how to google an error.

### What it means to "know how to program"

Most programmers can program in more than one language. That's because they know *how to program* generally, as opposed to "knowing" Python, R, Ruby, or whatever.

In other words, programming is an extendible skill. Basic programming concepts -- conditionals, for loops, functions -- can be found in almost any programming language.

That being said, programming languages differ from one another in the following ways:

1. **Syntax**: whether to add a semicolon at the end of each line, etc.
2. **Usage**: JavaScript is for building websites, R is for statistics, Python is general purpose, etc.
3. **Level**: how close you are to the hardware. 'C' is often considered to be the lowest (or one of the lowest) level languages.
4. **Object-oriented:** "objects" are data + functions. Some programming languages are object-oriented (e.g. Python) and some aren't (e.g. C).
5. **Many more**: Here's a [list](https://en.wikipedia.org/wiki/List_of_programming_languages_by_type) of all the types of programming languages out there.

So what should your first programming language be? That is, what programming language should you use to learn *how to program*? At the end of the day, the answer depends on what you want to get out of programming. Many people recommend Python because its fun, easy, and multi-purpose. Here's an [article](http://lifehacker.com/which-programming-language-should-i-learn-first-1477153665) that can offer more advice.

Regardless of what you choose, you will probably grow 'comfortable' in one language while learning the basic concepts and skills that allow you to 'hack' your way into other languages.  

Thus "knowing how to program" means learning how to *think* like a programmer, not necessarily knowing all the language-specific commands off the top of your head. **Don't learn specific programming languages; learn how to program.**

### What programming is like

![xkcd](http://sslimgs.xkcd.com/comics/wisdom_of_the_ancients.png)

Here's the sad reality: When you're programming, 80% or more of your time will be spent debugging, looking stuff up (like program-specific syntax, [documentation](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#documentation) for packages, useful functions, etc.), or testing. This does not just apply to beginner or intermediate programmers, although you will grow more "fluent" over time.

If you're a good programmer, you're a good detective!

### Debugging

1. Read the errors!
2. Read the documentation
2. Make it smaller
3. Figure out what changed
4. Check your syntax
5. Print statements are your friend

### Googling Errors

* google: name-of-program + text in error message
* Remove user- and data-specific information first!
* See if you can find examples that do and don’t produce the error

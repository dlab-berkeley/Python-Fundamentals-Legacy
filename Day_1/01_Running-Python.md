# Python Basics: 1 Running Python

> ## Questions
> How can I run Python programs?
>
> ## Learning Objectives
>
> *   Explain how the shell relates to other programs like Python.
> *   Open a Python interpreter from the shell.
> *   Run a Python script from the shell.
> *   Understand the importance of IDE's and program-specific tools.
> *   Find which version of Python is used by the interpreter.
> *   Start an iPython notebook server from the shell

## Running Python in Shell: Interactive Mode

If you took Programming FUN!damentals, you used the shell as the interface between us and the UNIX operating system.

But we can also use shell to interact with other programs. For example, we can run a Python interpreter right in shell. An **interpreter** is a program that reads and executes code. This includes source code and scripts.

~~~python
$ python

Python 2.7.6 (default, Mar 22 2014, 22:59:56)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
~~~

The `>>>` is Python's way of telling you that you are in **interactive mode**. In interactive mode, what you type is immediately run.

~~~python
>>> 5
5
>>> print(5*7)
35
>>> "hello" * 4
'hellohellohellohello'
>>> type("hello")
<type 'str'>
~~~

To escape the Python interpreter and go back to Shell, type

~~~python
>>> quit()
$
~~~

Notice that the terminal window will go back to bash, giving you a `$` prompt.

> #### Which Python?
>
>
> To see which version of Python you have, enter the command `which python` in
> bash. You can use the `which` command with other programs, too.

## Running Python in Shell: Normal Mode

Python has two basic modes: normal and interactive. Interactive mode allows you to test out and see what Python will do. If you ever feel the need to play with new Python statements, go into interactive mode and try them out.

If you quit from the Python interpreter and enter it again, the definitions you just made (functions and variables) are lost. Therefore, if you want to write a somewhat longer program, you are better off using a text editor to prepare the input for the interpreter and running it with that file as input instead.

This is known as creating a **script** (just like the shell scripts we created in Programming FUN!damentals). Python scripts have the ".py" extension to let everyone know (including the operating system) it is a Python program.

The normal mode is the mode where the scripted and finished .py files are run in the Python interpreter. To run a program, make sure you're in bash mode in your terminal (the default mode), `cd` into the directory in which the Python program (.py file) is located, and then enter the command `python [name of file]`. Here's an example from out GitHub repo:

~~~bash
$ python madlib.py
~~~

Once the program ends, it will give a `$` prompt, returning to bash mode.

## IDEs and other Tools

It's common to write python programs using either a text editor or an interactive/integrated development environment (IDE). An IDE  is a software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of a source code editor, build automation tools, and a debugger. Some of them come with package managers and other features, too.

There are many Python IDE's. You can see a comparison [here](https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments#Python)

> #### Editors v. IDEs
>
> Notepad++, Vim, SublimeText etc are text editors. They are not specific
> to Python, or to any other language. They are not an IDE. That said,
> these editors are extensible, and through the use of plugins they allow the
> user to implement IDE-like functionality for as broad a range of languages
> or syntaxes as plugin writers care to cover.

## Jupyter Notebooks

This course will be using a Jupyter Notebook to interact with Python.  The bit of extra setup is well worth it because the Notebook provides code completion and other helpful features.

Jupyter Notebooks are included in the Anaconda distribution which you installed. Notebook files have the extension ".ipynb" to distinguish them from plain-text Python programs.

To get started, first download the materials:

1. Go to our GitHub repo [here](https://github.com/dlab-berkeley/python-fundamentals).
2. Click on the green button in the top right that says "Clone or download".
3. Click "Download ZIP".
4. Unzip the file.
5. Move the unzipped 'python-fundamentals' (or 'python-fundamentals-master') to your Desktop.

Then open up Jupyter:

1. Open the Anaconda Navigator program on your computer.
2. Open Jupyter Notebook from there.
3. Navigate to the `python-fundamentals-master` folder. Depending on what your home directory is, this most likely mean clicking the "Desktop" folder, at which point `python-fundamentals-master` should be visible.
4. Click on `python-fundamentals-master`.
5. Click on `Day_1`.

This will start a Jupyter Notebook server and open your default web browser.

- The server runs locally on your machine only and does not use an internet connection.
- The server sends messages to your browser.
- The server does the work and the web browser renders the notebook.
- You can type code into the browser and see the result when the web page talks to the server.

This has several advantages:

- You can easily type, edit, and copy and paste blocks of code.
- Tab complete allows you to easily access the names of things you are using and learn more about them.
- It allows you to annotate your code with links, different sized text, bullets, etc., to make it more accessible to you and your collaborators.
- It allows you to display figures next to the code that produces them to tell a complete story of the analysis.
- The notebook is stored as JSON but can be saved as a .py file if you would like to run it from the bash shell or a python interpreter.
- Just like a webpage, the saved notebook looks different than what you see when it gets rendered by your browser.

Another way of starting a notebook server is through the command line. Make sure you're in the directory you want to be in, or a parent of it, then use the following command:

~~~bash
$ jupyter notebook
~~~

Let's get programming!

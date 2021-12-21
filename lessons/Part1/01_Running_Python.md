# Python Basics: Running Python

> ## Questions
> How can I run Python programs?
>
> ## Learning Objectives
>
> *   Running Python in IDEs
> *   Jupyter Notebooks
> *   Download the training material
> *   Open Jupyter Notebook


## Running Python in Integrated Development Environments

It's common to write Python programs using either a text editor or an integrated development environment (IDE). An IDE is a software application that provides a comprehensive suite of tools to programmers for software development. An IDE normally consists of a source code editor, build automation tools, and a debugger. Some of them come with package managers and other features, too.

There are many Python IDE's. You can see a comparison [here](https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments#Python).

## Jupyter Notebooks

In this course, we interact with Python using Jupyter Notebooks. Using Jupyter Notebooks will require some extra setup. It will be well worth it, however, as Jupyter Notebooks are among the most powerful (and heavily used) tools for conducting data science in Python.

Jupyter Notebooks are included in the Anaconda distribution which you installed. Notebook files have the extension ".ipynb" to distinguish them from plain-text Python programs.

## Download the training material

1. Go to our GitHub repo. The URL is [**https://github.com/dlab-berkeley/python-fundamentals**](https://github.com/dlab-berkeley/python-fundamentals)
2. Click on the green button in the top right that says "Clone or download".
3. Click "Download ZIP".
4. Unzip the file.
5. Move the unzipped 'python-fundamentals' (or 'python-fundamentals-master') to your Desktop.

## Open Jupyter Notebook

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

Let's get programming!

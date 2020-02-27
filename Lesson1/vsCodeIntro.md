# Overview:

* Getting started with VS Code and python
* Getting Started with Virtualenv

# Intro To VSCode - 1

Basic orientation.  Will cover more of this later once we get into 
code editing as some of those features will be more applicable then.

This lesson will loosely follow the VS code [getting started with the userinterface doc](https://code.visualstudio.com/docs/getstarted/userinterface)

## Why VSCode

* Lightweight
* feature rich
* multiplatform platforms
* Free and opensource
* lowest common denominator

## Why use an IDE

* Nobody uses vi to write briefing notes.
* Why would you use a text editor for writing code.
* designed to make your job easier...   
* ... if not initially in the long run for sure.

## Sidebar / Activity Bar

* Review Sidebar / Activity Bar - Only options we may use in this course.
    * explorer
    * search and destroy (replace)
    * git 
    * debugger
    * testing
    * Extensions

## Explorer / Python development

* choose explorer view
* "Side Bar" ironically on the bottom.
* "Status Bar" at bottom
* open a few files
* drag them around
* Demo "preview" for markdown
* open Terminal
* demo selection of default shell

## Go over view menu options

* not so Zen Mode.
    * _View->Appearance->Zen Mode_
    * Remember _ESC_ _ESC_ to exit
* F11 to go in and out of full screen 
* wordwrap option
* minimap option

## Extensions
* python for sure
* other ones that I like:
   * **Code Spell Checker:** helps you avoid Spalling Misteaks
   * **autoDocString:** helps you write useful comments in your code.

# VirtualEnv and PIP

Allows for isolation of dependencies between projects.

* Python comes with a lot builtin.  
* Avoid re-inventing the wheel and re-use code wherever possible.
* Each project may have different set of requirements.
* projects may have the same module requirement but different versions.
* virtualenv helps and is great.

### Other options to accomplish similar functionality:
* pipenv
* conda
* anaconda
* Hacking it yourself by modifying paths (not advised)

## Install Virtualenv

### Confirm python version

* open a terminal
* type `python` and ensure that resolves to python 3 version, ie output looks similar to: 

```python
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

* The >>> indicates you are using python interactive mode.
    * to exit type: `exit()`
    * or ctrl->z

### Install Virtualenv (Windows)

```
python -m virtualenv venv
```

### Install Virtualenv (Mac/Linux)

```
virtualenv -p python3 venv
```

## Activate Virtualenv

VSCode should auto detect any virtualenv that is called *venv*. 

The following instructions show you how to do it manually

### Windows

1. Open Terminal
1. navigate to `venv/scripts
```







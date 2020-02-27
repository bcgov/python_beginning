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

## Run Scripts
* open hello.py
* run the script by pressing the _green arrow_ at top right.
* run by pressing `F1` and type: `python: Run Python File in Terminal`
* right click->Run Python File in Terminal
* go to terminal and press `up arrow` to get last command and enter to re-run.

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

_You may get popups when you run the following... Say NO_

```
python -m virtualenv venv
```

* now we are going to tell VSCode to use this virtualenv
* Either press python option in the sidebar, or
* `ctrl->P` and select `Python: Select Interpreter`
* Select the venv version
* open hello.py and run that script
* demo where the settings are in the folder `.vscode/settings.json`


### Install Virtualenv (Mac/Linux/WSL)

```
python -m virtualenv venv
```

### Manually configure the venv for you project.

* open `vscode/settings.json`
* add the following line:

```
...
"python.pythonPath": "<path to virtualenv>", 
...
```

### Activate Virtualenv

* with VSCode you shouldn't need to do this, especially if you named your virtualenv `venv`
* You will need to do these steps if you build/deploy your code to Jenkins/Github Actions/Openshift.
* to simulate this you can run these commands 

#### Activate on Windows
```
cd <to project dir>
.\venv\Scripts\activate.bat
```

#### Activate on a normal os (linux/wsl/osx)
```
cd <to project dir>
source venv/bin/activate
```

### Run hello.py

* Open hello.py
* run hello.py
* notice that the prompt has (venv) in front.

# Install Training Course Dependencies into Virtualenv

* Open a terminal if you don't already have one open
* Make sure its using the virutalenv, prompt should look similar to what is shown below.  Make sure you can see `(venv)` at the start of the prompt

``` 
(venv) @ C:\training\python
$ 
```

* install the training dependencies:

```
pip install -r requirements.txt
```

## Python Interactive window

### Create an Interactive Window

* open a terminal
* type `python`

```
(venv) @ C:\Kevin\proj\python_training
$ python
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

* `>>>` is the python prompt.
* to exit either:
    *  type: `exit()`
    * ctrl->z->enter

### [Getting Help](https://developers.google.com/edu/python/introduction#online-help,-help-,-and-dir)

* google your question
* search stack exchange directly
* Read the docs at [python.org](https://docs.python.org/3/)
* use the built in `help` and `dir` functions

You can never go wrong with an o'reilley book:

<img src="https://covers.oreillystatic.com/images/0636920028154/cat.gif">

http://shop.oreilly.com/product/0636920028154.do



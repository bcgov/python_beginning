# Introduction

This document is a drop box where I can scribble down ideas relating 
to the training, allowing me to then come back and address them at a 
later date.

During the development of the training material it helps me ensure that
all the various topics that I think need to be covered are in fact covered.

# Ideas on topics to include in training

* markdown, what is it, how does it work
* versioning in requirements
* Getting set up w/ Virtualenv
* Configure environmments in vscode and add to .gitignore to help manage secrets.
* Secret management, retrieve environments variables.
* Git in vscode, how to commit.
* help demo on different function
* imports, os.path, os, shutil, re, logging, 
* review basics of git
* ininstance( for strings)
* type()
* using these with if
* try except 
* get g+t for Michelle (size large)
* databases?
* lists lesson, add some more smaller exercises into the lesson.
* remove output from notebooks
 

## lesson flow:
    ...
    working with files
    dictionaries
    utilities / pypi / imports
    apis

* docstrings make part of utilities
* pprint with the dict / json lesson
* dates

# Improvements

Comments here are ideas I have about how to make the training better next time:

## Ditch Jupyter and virtualenv from the requirements

To get jupyter set up requires setting of a virtualenv, which ended up 
eating up a lot of time trying to deal with installation issues on some 
computers.  Thinking we can ditch that requirement if we move the jupyter 
markdown text to lectures markdown files, and include links to code files
from the markdown.

Running code from files seemed to work better.

* Move the virtualenv lesson to utilities
* Identify the config changes required to be run
    ```
    Set-ExecutionPolicy RemoteSigned
    ```
* make installing requests module part of pre-reqs.
* after those changes are made make decision around whether git overview
  could be moved to utilities.
* review utilities lesson... If anything felt like this lesson could be trimmed and possibly deleted.  May be more pertinent if we move virtualenv and pip lessons there. 

* virtualenv/pip would fit nicely in lessons as we could install requests there which is what is required for api lesson
* getting VS code to work with virtualenv was another place we ran into snags
* Think if there is a way to make that part go more smoothly
  (script that reads the registry, gets the python install path and updates the .settings file itself? )

## Emphasize Choco Install

The choco installs had way less configuration issues as the various
manual installs that people ran on their own.  Going forward the 
recommendation will be to uninstall and use choco to install, unless you 
put yourself in the super advanced category for sys admin on your windows box.

## strings and numbers

* felt like we spent too much time on this lesson. 

## put together a cheat sheet

* quick summary of everything we are learning in the course that people 
could refer to.
* look to see if something already exists.

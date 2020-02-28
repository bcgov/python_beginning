# Overview:

* Getting started with VS Code and python
* Getting Started with Virtualenv

# Intro To VSCode - 1

<img src="https://lh3.googleusercontent.com/fpy1e4CEAG7bdNMGihezo_-eTUj_w5nyoYT8lrT-KT6w4AstNaool4Ny7R4aFzhjkjpkgJdLfLNNAmHqjWVrV_2zaY0GFfOB9euEAu32cgdPtdazbDuVVoKEZgrXGPnCfDMGeL8lUeAnuwC_WkBVmRkbzeCjyDBJBGvZtBlWZfhq4t7Y0nAJtQjM9oljH1f5gKPMkO_pIUCeaE0GCRBPFZrQ4cLGDSd-PBsod-tsWuCNrmY5jRl9pDmmzlnesBTMUcWCtoAoqKPAjHYSjwDY218sjl4InELb1_fkpx907y30WXjYu54cyoXOfg39roNWJ9iMqWztoOPJh8JDXcBQjcYYXon8774AfJEmYkmiOYUdq4rl_X5QAH7b1P2xkcBpymp_wVy35RbZrG4w_MVw7mDSdbudHPCaaChLyNRcZXQLgVhF2S1tJ1vi59e1gJlu9HRly-zE_3Z518PCG3CAu9v0qpAWkAmvRYZ3Q16BZz5cQ4Oj6XVNXILyVTq1OMy108ukWBsBC981aRuPPzLv8_Iaa7xShfkCr02qDifJEoqw-fuD5l6Bl9B4lxCWbhjuVbbQoq23YA2265Tm5Oc0Z0r8NGF6i5ctWjnTAQk94ZrwSGoRScXqJsvR4vxTvqLyPB729TVq2GHfk5qxeEyGzX1zEOjfHBCcuskmSWFywih3D5jg8x0ULmpYo74WsjvfFbi2h18Twf4blxPD_qcniC0n_QJr4_OgHg2OVRPKxiQ7Rwu8=w716-h954-no" width=200>

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

<img src="https://lh3.googleusercontent.com/3bOtUqtA9fOXILN0ajd6AEXFVxV9ItxaHjQvryHdnVA98PUFxr_0csykpFSRYd69Ur6gsJ4QEamj_pnxC713QVVHLpjrsEuAd8VVU6OFI4QCdbT3WTOUKAqeiah1eqDTTITePy_fqj8zcOSkvdYxWlWDRLkOWF92zZsMemCeP3OV0YqutCDK8VbqB9g9NX59v1Q6QnSSgoRZvPUzRsVnJw1HEFcdgoHYEWPfVVjACgUxJ9JC_3nZVwoz8j4nod7PBw30mLfv13zKClSFUKQCCCkhG8GpHEC7ZwYqIWzOF4HMEwRaVrut4dvJaDjLnml_I9foBpwzjYqS97-i5lMFYIA4yt9GW1aLq_6KKEyzl0rexrCAZWec6U7KWzAEkHc20XMxOh9-2ncV2I2tfcZdr2CsN0NHUPjbpBOO6VZuu1cPniU8xPuOIaAPZ01LHfktklxOsSxBft1IrB0s18HNENqaMPqsu4b2bEZc45rV7pxj_9fFcH6X6d1hws9uvqiNUYIXhdyKCBcSAOlw8uCEoJ2v9Ku74kuYyTp4LaNRJWm0gN6U6skwSuAE6mJnGlyXUwMb3gtPuibm7qtGg51548wPCdgY8ICCqljXbnjZ51c3zX8T7nTbiVjGr797nOyZecoF0-jMGF8lxthKu6J_cG_KXa5iMkiBRHxHdipzVcx8q7BkCjqwO3pJNQEkYUkLeiQrc5U-EEsiLLgD3ujaQdytq3Q2CnzxgaZQVMJiZSdVoI5z=w1272-h954-no" width=400>

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

<img src="https://lh3.googleusercontent.com/DGKU-YguC7x9ZUkMMIP11HePEvOcZ7aFXzqlLzpsgbwRZel4UhaDhmO47oBBqLEr4GI9unbmJvIhKBPqkR1RtEKQHa6x16Qta8M_7liJcTrmUt0MwSHIS2n0bXgroPJ-eqDqZLWgCNQiCUSbASPVl8LfPdj3x56DZVKBcWkUEeT-pzXFc8xgE5R4SPomBorS4IZ0-Ic9aqf8qKTVG6tywUO2AUxM6ALja05WCN7HWJb_MWS3MuBbfFQf4GvIbGlpNXKxfWEDCSbWBahpPjgHk1Adt-ZtdDnT2RvSvLIXeHhyL-8-_tH6ZlVraSI5yP_2OzMpwj-CqAyNISgVH359IPCxRk0wew8n6iZnxIdccUb3div-oN6hY9XxYuZJzbMRldhQ8PgV_MRaMcYbGp4erbLH7O6frDBfI38GSyKs5TOeWgIU9uPNu42_siMUmN79yTd422yMSqLyGTs9hCNPRzkIRpda_04str5ZNlEpm8SJ9-aRSMHJLi9I0WVDrGD8-WRHeExWqYJwrro8XFWBljEiA0Iw1aIped6Byj30XHnK5yGBhM-vD58TUyHfvFrJ_c2H-8aeSWNImM8Vc7Fo23gaETG5RC6elmxsujsPVzUMTiCWJz4r6c_ihf2nQ8465NooirnzQM64UC1JuYhTzZISPArOPEs6vQMPmvl5GQYcNaw5Da7Q9zzHitknoOMA4_RAvb7hq7zGm0BuA7d_w5n1Vwza3kilbkBDQ9Xav6pcAA4G=w1017-h763-no" width=500>

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

You can never go wrong with an o'reilly book:

<img src="https://covers.oreillystatic.com/images/0636920028154/cat.gif">

http://shop.oreilly.com/product/0636920028154.do



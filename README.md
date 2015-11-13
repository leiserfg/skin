```lisp
	 _______  _       _________ _       
	(  ____ \| \    /\\__   __/( (    /|
	| (    \/|  \  / /   ) (   |  \  ( |
	| (_____ |  (_/ /    | |   |   \ | |
	(_____  )|   _ (     | |   | (\ \) |
	      ) ||  ( \ \    | |   | | \   |
	/\____) ||  /  \ \___) (___| )  \  |
	\_______)|_/    \/\_______/|/    )_)

```                                    
Skin is a project template renderer (something like PasteScript but without Paste itself) powered by ~~Jinja2 and~~ a lot of needs of something like it.



Installing
==========

Install download this repo (or clone it) and just python setup.py install.


Usage
=====

* List templates `skin -l`
* Render a template `skin template_name`
* Bash completion `skin -b >> ~/.profile`
* Zsh completion `skin -z >> ~/.zshrc`


If you wanna add templates, just make one and add it to your own ~/.skin folder.


Contributing
============

Clone it, install in development mode

```shel
pip install -e .
```
and, hack on it!
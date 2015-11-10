```
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


Hacking
=======

Development
-----------

pip install . -e

Architecture
-----------
Skin will be rewritten, the new architecture will be like this:
|file         | use                                                                       |
------------------------------------------------------------------------------------------
| templates.py| define the Template class with all the template stuff                     |
| utils.py    | functions used on the lib and/or the rules                                |
| core.py     | managing of the project template, rendering of a specific project template|
| cli.py      | the whole thing :D                                                        |
| _compat.py  | things to make source usable y both pythons (2 and 3)                     |

Other files are still here for take code :D they will be removed sooner or latter 
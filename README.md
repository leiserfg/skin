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
Skin will be rewrited, the new architecture will be like this:
templates.py -> provide a render function that render a unicode template from a data (dict with values)
utils.py -> functions used on the lib and/or the rules
core.py -> managin of the rules, rendering of a specific rule.
cli.py -> the whole thing :D
_compat.py -> things to make source usable y both pythons (2 and 3)

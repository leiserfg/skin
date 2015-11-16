# -*- coding: utf-8 -*-

from datetime import date
import getpass 


fullname = prompt('Full module name (as package.module): ')
name = fullname.split('.')[-1]
description = prompt('Package description: ')
year = prompt(u"© Year: ", date.today().year)
author = prompt("Author: ", getpass.getuser())
license = prompt('Project licence', 'BSD License')

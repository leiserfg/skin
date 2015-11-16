# -*- coding: utf-8 -*-
"""
    skin.__init__
    ~~~~~~~~~

    There is the version of the package.

    :copyright: (c) 2014 by the Leiser Fernández Gallo.
    :license: BSD License.
"""

from datetime import datetime
today = datetime.now().date().isoformat().replace('-', '')
__version__ = '1.0-dev-%s' % today

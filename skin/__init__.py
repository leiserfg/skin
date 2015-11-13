# -*- coding: utf-8 -*-

from datetime import datetime
today = datetime.now().date().isoformat().replace('-', '')
__version__ = '1.0-dev-%s' % today

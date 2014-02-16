# -*- coding: utf-8 -*-

from datetime import datetime
today = datetime.now().date().isoformat().replace('-', '')
__version__ = '0.4-dev-%s' % today

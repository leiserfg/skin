from datetime import datetime
today = datetime.now().date().isoformat().replace('-','')
__version__ = '0.3-dev-%s' % today
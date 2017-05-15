import os
import sys
sys.path.append('/home/ogh/work/tapache/ogh')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ogh.settings'
print sys.version_info

import django
django.setup()
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

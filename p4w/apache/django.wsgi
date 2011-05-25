import os
import sys

sys.path.append('/home/johan/srv')
sys.path.append('/home/johan/srv/wetart/p4w')

os.environ['DJANGO_SETTINGS_MODULE'] = 'p4w.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
import os
import sys
import site

site.addsitedir('/home/johan/.virtualenvs/wetart/lib/python2.6/site-packages')

sys.path.append('/home/johan/srv/wetart')
sys.path.append('/home/johan/srv/wetart/p4w')

os.environ['DJANGO_SETTINGS_MODULE'] = 'p4w.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
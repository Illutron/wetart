import os
import sys
import site

site.addsitedir('/home/wetart/.virtualenvs/wetart/lib/python2.6/site-packages')

sys.path.append('/home/wetart/srv/')
sys.path.append('/home/wetart/srv/wetart/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'wetart.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
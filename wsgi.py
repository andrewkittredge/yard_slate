import os
import sys

from django.core.handlers.wsgi import WSGIHandler

sys.path.append('/home/yardslate/webapps/yard_slate/myproject/myproject')

os.environ['DJANGO_SETTINGS_MODULE'] = 'yard_slate.settings'
application = WSGIHandler()

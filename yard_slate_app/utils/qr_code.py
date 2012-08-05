'''
Created on Jul 25, 2012

@author: akittredge
'''

from django.conf import settings
from urlparse import urljoin
slate_domain = settings.SLATEDOMAIN

def qr_url(slate, width=150, height=150):
    slate_url = '/'.join(('http://', 
                             slate_domain, 
                             'view_slate/?yard_slate=%s' % slate.id))
    return 'http://api.qrserver.com/v1/create-qr-code/?size=%d*%d&data=%s' % (width,
                                                                              height,
                                                                              slate_url)
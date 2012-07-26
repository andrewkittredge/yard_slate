'''
Created on Jul 25, 2012

@author: akittredge
'''



def qr_url(slate, width=150, height=150):
    return 'http://api.qrserver.com/v1/create-qr-code/?size=%d*%d&data=%s' % (width,
                                                                              height,
                                                                              slate.id)
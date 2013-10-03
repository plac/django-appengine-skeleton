'''
Created on 03/10/2013

@author: pedro
'''

from django.conf.urls.defaults import *
from guestbook.views import main_page, sign_post 

urlpatterns = patterns('',
    (r'^sign/$', sign_post),
    (r'^$', main_page),
)
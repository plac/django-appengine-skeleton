'''
Created on 03/10/2013

@author: pedro
'''
from google.appengine.ext import db

class Greeting(db.Model):
    """ Models an individual Guestbook entry with an aouthor, content and date. """
    author = db.StringProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)
    
    @classmethod
    def get_key_from_name(cls, guestbook_name=None):
        return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')

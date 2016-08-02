from google.appengine.ext import ndb
from protorpc import messages

class User(ndb.Model):
   """User Profile"""
   name = ndb.StringProperty(required=True)
   email = ndb.StringProperty(required=True)
   wins = ndb.IntegerProperty(default=0)
   games_played = ndb.IntegerProperty(default=0)

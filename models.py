from google.appengine.ext import ndb
from protorpc import messages

class User(ndb.Model):
   """User Profile"""
   user_name = ndb.StringProperty(required=True)
   email = ndb.StringProperty(required=True)
   wins = ndb.IntegerProperty(default=0)
   games_played = ndb.IntegerProperty(default=0)
   

class Game(ndb.Model):
   """Game Object"""
   player1 = ndb.KeyProperty(required=True, kind='User')
   player2 = ndb.KeyProperty()
   player3 = ndb.KeyProperty()
   player4 = ndb.KeyProperty()
   player5 = ndb.KeyProperty()
   player6 = ndb.KeyProperty()
   player1VictoryPoints = ndb.PicklePropert()
   player2VictoryPoints = ndb.PicklePropert()
   player3VictoryPoints = ndb.PicklePropert()
   player4VictoryPoints = ndb.PicklePropert()
   player5VictoryPoints = ndb.PicklePropert()
   player6VictoryPoints = ndb.PicklePropert()
   player1CollectionPoints = ndb.PicklePropert()
   player2CollectionPoints = ndb.PicklePropert()
   player3CollectionPoints = ndb.PicklePropert()
   player4CollectionPoints = ndb.PicklePropert()
   player5CollectionPoints = ndb.PicklePropert()
   player6CollectionPoints = ndb.PicklePropert()
   game_over = ndb.BooleanProperty(required=True, default=False)
   winner = ndb.KeyProperty(required=True, kind='User')


class UserForm(messages.Message):
   """User Form"""
   user_name = messages.StringField(1, required=True)
   email = messages.StringField(2)
   wins = messages.IntegerField(3, required=True)
   games_played = messages.IntegerField(4, required=True)


class GameForm(messages.Message):
   """GameForm for outbound game state information"""
   urlsafe_key = messages.StringField(1, required=True)
   next_move = messages.StringField(2, required=True)
   player1 = messages.StringField(3, required=True)
   player2 = messages.StringField(4)
   player3 = messages.StringField(5)
   player4 = messages.StringField(6)
   player5 = messages.StringField(7)
   player6 = messages.StringField(8)


class NewGameForm(messages.Message):
   """Used to create a new game"""
   player1 = messages.StringField(1, required=True)
   player2 = messages.StringField(2)
   player3 = messages.StringField(3)
   player4 = messages.StringField(4)
   player5 = messages.StringField(5)
   player6 = messages.StringField(6)


class StringMessage(messages.Message):
    """Single outbound string message"""
    message = messages.StringField(1, required=True)


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
   player_1 = ndb.KeyProperty(required=True, kind='User')
   player_2 = ndb.KeyProperty()
   player_3 = ndb.KeyProperty()
   player_4 = ndb.KeyProperty()
   player_5 = ndb.KeyProperty()
   player_6 = ndb.KeyProperty()
   player_1_points = ndb.PicklePropert()
   player_2_points = ndb.PicklePropert()
   player_3_points = ndb.PicklePropert()
   player_4_points = ndb.PicklePropert()
   player_5_points = ndb.PicklePropert()
   player_6_points = ndb.PicklePropert()
   player_1_collection_points = ndb.PicklePropert()
   player_2_collection_points = ndb.PicklePropert()
   player_3_collection_points = ndb.PicklePropert()
   player_4_collection_points = ndb.PicklePropert()
   player_5_collection_points = ndb.PicklePropert()
   player_6_collection_points = ndb.PicklePropert()
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
   player_1 = messages.StringField(3, required=True)
   player_2 = messages.StringField(4)
   player_3 = messages.StringField(5)
   player_4 = messages.StringField(6)
   player_5 = messages.StringField(7)
   player_6 = messages.StringField(8)


class NewGameForm(messages.Message):
   """Used to create a new game"""
   player_1 = messages.StringField(1, required=True)
   player_2 = messages.StringField(2)
   player_3 = messages.StringField(3)
   player_4 = messages.StringField(4)
   player_5 = messages.StringField(5)
   player_6 = messages.StringField(6)


class StringMessage(messages.Message):
    """Single outbound string message"""
    message = messages.StringField(1, required=True)


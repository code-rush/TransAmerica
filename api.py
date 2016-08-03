import endpoints

from protorpc import remote, messages

from google.appengine.ext import ndb

from models import User, Game
from models import UserForm, GameForm, NewGameForm, StringMessage


NEW_GAME_REQUEST = endpoints.ResourceContaincer(NewGameForm)
GET_GAME_REQUEST = endpoints.ResourceContaincer(
           urlsafe_game_key=messages.StringField(1))
USER_REQUEST = endpoints.ResourceContaincer(user_name=messages.StringField(1),
                                            email=messages.StringField(2))


@endpoints.api(name='TransAmerica', version='v1')
class TransAmericaGameAPI(remote.Service):
   """Game API"""
   @endpoints.method(USER_REQUEST,
                     StringMessage,
                     name='create_user',
                     path='users',
                     http_method='POST')
   def create_user(self, request):
       """Creates a user"""
       if User.query(User.user_name == request.user_name).get():
           raise endpoints.ConflictException(
                   'A user with that name already exists!')
       user = User(user_name=request.user_name, email=request.email)
       user.put()
       return StringMessage(messages='User {} successfully created'\
                             .format(request.user_name))


api = endpoints.api_server([TransAmericaGameAPI])
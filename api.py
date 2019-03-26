import endpoints

from protorpc import remote, messages

from google.appengine.ext import ndb

from models import (User, Game, UserForm, GameForm, NewGameForm, 
                    StringMessage)

NEW_GAME_REQUEST = endpoints.ResourceContaincer(NewGameForm)
GET_GAME_REQUEST = endpoints.ResourceContaincer(
           urlsafe_game_key=messages.StringField(1))
USER_REQUEST = endpoints.ResourceContaincer(user_name=messages.StringField(1),
                                            email=messages.StringField(2))


_zone1 = []
_zone2 = []
_zone3 = []
_zone4 = []
_zone5 = []

_zone1Full = []
_zone2Full = []
_zone3Full = []
_zone4Full = []
_zone5Full = []

_playersHubSelections = []

@endpoints.api(name='TransAmerica', version='v1')
class TransAmericaGameAPI(remote.Service):
   """Game API's"""
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


   @endpoints.method(GET_GAME_REQUEST, GameForm, name='get_game',
                      path='game/{urlsafe_game_key}', http_method='GET')
    def get_game(self, request):
        """Return the current game state"""
        game = get_by_urlsafe(request.urlsafe_game_key, Game)
        if game:
            return game.to_form()
        else:
            raise endpoints.NotFoundException('Game not found!')


   @endpoints.method(NEW_GAME_REQUEST, GameForm, name='new_game',
                      path='game', http_method='POST')
    def new_game(self, request):
        """Creates new game"""
        user_a = User.query(User.name == request.user_a).get()
        user_b = User.query(User.name == request.user_b).get()
        if not user_a and user_b:
            raise endpoints.NotFoundException('One of the users does not exist!')

        game = Game.new_game(user_a.key, user_b.key)
        return game.to_form()


api = endpoints.api_server([TransAmericaGameAPI])
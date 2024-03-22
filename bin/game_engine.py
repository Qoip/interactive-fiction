'''Module containing GameEngine class.'''

from content_generator import ContentGenerator
from game_state import GameState
from data_storage import DataStorage
from game_settings import GameSettings


class GameEngine:
    '''Main game manager.'''

    state = GameState()
    __storage = DataStorage()
    __content_generator = ContentGenerator()

    def user_query(self, message: str):
        '''Resolve user game query.'''

    def reset_state(self):
        '''Resets game.'''

    def settings_change(self, settings: GameSettings):
        '''Update settings.'''

    def change_category_element(self, category: str):
        '''Change current element by category.'''

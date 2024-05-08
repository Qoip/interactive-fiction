'''Module containing GameEngine class.'''

from content_generator import ContentGenerator
from game_state import GameState
from data_storage import DataStorage


class GameEngine:
    '''Main game manager.'''

    def __init__(self):
        self.state = GameState()
        self.__storage = DataStorage()
        self.__content_generator = ContentGenerator(self.state)

    def user_query(self, message: str):
        '''Resolve user game query.'''

    def reset_state(self):
        '''Resets game.'''

    def change_category_element(self, category: str):
        '''Change current element by category.'''

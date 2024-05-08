'''Module containing GameEngine class.'''

from content_generator import ContentGenerator
from game_state import GameState
from data_storage import DataStorage
from message import Message
import json


class GameEngine:
    '''Main game manager.'''

    def __init__(self):
        self.state = GameState()
        self.__storage = DataStorage()
        self.__content_generator = ContentGenerator(self.state, self.__storage)

    def user_query(self, message: str) -> str:
        '''Resolve user game query and return next message.'''
        response = self.__content_generator.user_query(message)
        data = json.loads(response.message)
        if "bars" in data:
            self.state.bars = data["bars"]
        if "location" in data:
            self.state.image_link = self.__content_generator.image_generate(data["location"])
        self.state.add_message(Message("assistant", data["response"]))
        return data["response"]

    def reset_state(self):
        '''Resets game.'''
        self.state.reset()
        # self.__storage.reset()

    # def change_category_element(self, category: str):
    #     '''Change current element by category.'''

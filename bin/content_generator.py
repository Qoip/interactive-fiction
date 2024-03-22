'''Module containing ContentGenerator class.'''

from message import Message
from game_state import GameState


class ContentGenerator:
    '''Provides API for resolving game queries.'''

    __game_state: GameState  # GameState link!

    def user_query(self, user_message: str) -> Message:
        '''Query to chatGPT from user.'''

    def system_query(self, system_message: str) -> Message:
        '''Query from system to category items clarify or storyline intervention.'''

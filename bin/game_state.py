'''Module containing GameState class.'''

from typing import List, Any  # remove Any
from game_settings import GameSettings
from message import Message


class GameState:
    '''Class responds to saving game current state.'''

    _game_settings: GameSettings # privateness?
    __last_messages: List[Message]
    __system_context: List[Message]
    __bars_info: Any  # json!

    def __init__(self):
        self.__load_from_file()

    def get_context_messages(self) -> List[Message]:
        '''Return messages needed for context.'''

    def add_message(self, message: Message):
        '''Add message to message history.'''

    def get_system_context(self) -> List[Message]:
        '''Return system context messages.'''

    def add_system_context(self, message: Message):
        '''Add message to system context messages.'''

    def get_bars(self) -> Any:  # json object!
        '''Return bars information.'''

    def set_bars(self, bars_info):
        '''Update bars.'''

    def reset(self):
        '''Reset all information to clear game state.'''

    def set_game_settings(self, settings: GameSettings):
        '''Update game settings.'''

    def __save_to_file(self):
        '''Save state to file.'''

    def __load_from_file(self):
        '''Load state from file.'''

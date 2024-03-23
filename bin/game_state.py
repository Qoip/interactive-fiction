'''Module containing GameState class.'''

from typing import List, Dict, Any
from pickle import dump, load
from game_settings import GameSettings
from message import Message


class GameState:
    '''Class responds to saving game current state.'''

    DEFAULT_SETTINGS_PATH = "./data/default_settings.json"

    __game_settings: GameSettings
    __last_messages: List[Message]
    __system_context: List[Message]
    __bars_info: Dict[str, Any]

    def __init__(self):
        self.__saving_path = "./data/settings.json"
        self.__load_from_file()

    def __del__(self):
        self.__save_to_file()

    def context_messages(self) -> List[Message]:
        '''Return messages needed for context.'''
        return self.__last_messages[:self.__game_settings.context_messages]

    def add_message(self, message: Message):
        '''Add message to message history.'''
        self.__last_messages.append(message)
        if len(self.__last_messages) > self.__game_settings.history_length:
            self.__last_messages = self.__last_messages[:self.__game_settings.history_length]
        self.__save_to_file()

    @property
    def system_context(self) -> List[Message]:
        '''Return system context messages.'''
        return self.__system_context

    def add_system_context(self, message: Message):
        '''Add message to system context messages.'''
        self.__system_context.append(message)
        self.__save_to_file()

    @property
    def bars(self) -> Dict[str, Any]:
        '''Return bars information.'''
        return self.__bars_info

    @bars.setter
    def bars(self, bars_info):
        '''Update bars.'''
        self.__bars_info = bars_info
        self.__save_to_file()

    @property
    def game_settings(self) -> GameSettings:
        '''Returns game settings'''
        return self.__game_settings

    @game_settings.setter
    def game_settings(self, settings: GameSettings):
        '''Update game settings.'''
        self.__game_settings = settings
        self.__save_to_file()

    def reset(self):
        '''Reset all information to clear game state.'''
        self.__load_from_file(self.DEFAULT_SETTINGS_PATH)
        self.__save_to_file()

    def __save_to_file(self):
        '''Save state to file.'''
        with open(self.__saving_path, 'wb') as state_storage:
            dump(self.__dict__, state_storage)

    def __load_from_file(self, file_path=None):
        '''Load state from file.'''
        file_not_found = False
        if file_path is None:
            file_path = self.__saving_path

        try:
            with open(self.__saving_path, 'rb') as state_storage:
                data = load(state_storage)
        except FileNotFoundError as exc:
            file_not_found = True
            if file_path == self.DEFAULT_SETTINGS_PATH:
                raise FileNotFoundError(f"No default game state file {file_path}.") from exc

        if not data or file_not_found:
            print(f"No data in game state file or file not found: {file_path}")
            if file_path == self.DEFAULT_SETTINGS_PATH:
                raise ValueError(f"No data in default game state file or not found: {file_path}")
            self.__load_from_file(self.DEFAULT_SETTINGS_PATH)
        else:
            self.__dict__.update(data)

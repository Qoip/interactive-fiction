'''Module containing GameState class.'''

from typing import List, Dict, Any
from json import dump, load, JSONDecodeError
from game_settings import GameSettings
from message import Message


class GameState:
    '''Class responds to saving game current state.'''

    DEFAULT_SETTINGS_PATH = "./static/default_state.json"

    def __init__(self):
        self.__game_settings = GameSettings()
        self.__message_history: List[Message] = []
        self.__system_context: List[Message] = []
        self.__bars: Dict[str, Any] = {}
        self.__saving_path = "./data/state.json"
        self.__image_link: str = None
        self.__load_from_file()

    def context_messages(self) -> List[Message]:
        '''Return messages needed for context.'''
        return self.__message_history[:self.__game_settings.context_messages]

    def add_message(self, message: Message):
        '''Add message to message history.'''
        self.__message_history.append(message)
        if len(self.__message_history) > self.__game_settings.history_length:
            self.__message_history = self.__message_history[:self.__game_settings.history_length]
        self.__save_to_file()

    def get_history_text(self) -> List[str]:
        '''Return message history.'''
        result = []
        for message in self.__message_history:
            result.append(message.message)
        return result

    @property
    def system_context(self) -> List[Message]:
        '''Return system context messages.'''
        return self.__system_context

    def add_system_context(self, message: Message):
        '''Add message to system context messages.'''
        self.__system_context.append(message)
        self.__save_to_file()

    @property
    def image_link(self) -> str:
        '''Return image link.'''
        return self.__image_link

    @image_link.setter
    def image_link(self, link: str):
        '''Set image link.'''
        self.__image_link = link
        self.__save_to_file()

    @property
    def bars(self) -> Dict[str, Any]:
        '''Return bars information.'''
        return self.__bars

    @bars.setter
    def bars(self, bars_info: Dict[str, Any]):
        '''Update bars.'''
        self.__bars = bars_info
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

    def to_json(self) -> Dict[str, Any]:
        '''Converts game state to json object'''
        return {
            "game_settings": self.__game_settings.to_json(),
            "message_history": [message.to_json() for message in self.__message_history],
            "system_context": [message.to_json() for message in self.__system_context],
            "bars": self.__bars,
            "image_link": self.__image_link
        }

    def from_json(self, json: Dict[str, Any]):
        '''Loads game state from json object'''
        try:
            self.__game_settings.from_json(json["game_settings"])
            # self.__message_history = [Message("", "").from_json(message)  # cringe
            #                           for message in json["message_history"]]
            # self.__system_context = [Message("", "").from_json(message)  # cringe
            #                          for message in json["system_context"]]
            self.__message_history = []
            for message_data in json["message_history"]:
                self.__message_history.append(Message("", ""))
                self.__message_history[-1].from_json(message_data)
            self.__system_context = []
            for message_data in json["system_context"]:
                self.__system_context.append(Message("", ""))
                self.__system_context[-1].from_json(message_data)
            self.__bars = json["bars"]
            self.__image_link = json.get("image_link", None)
            self.__save_to_file()
        except KeyError as exc:
            raise KeyError(f"JSON decode error:\n{json}") from exc

    def __save_to_file(self):
        '''Save state to file.'''
        with open(self.__saving_path, 'w', encoding='utf-8') as state_storage:
            dump(self.to_json(), state_storage, indent=4)

    def __load_from_file(self, file_path=None):
        '''Load state from file.'''
        file_not_found = False
        if file_path is None:
            file_path = self.__saving_path

        data = None
        try:
            try:
                with open(file_path, 'r', encoding='utf-8') as state_storage:
                    data = load(state_storage)
            except JSONDecodeError:
                pass
        except FileNotFoundError as exc:
            file_not_found = True
            if file_path == self.DEFAULT_SETTINGS_PATH:
                raise FileNotFoundError(f"No default game state file {file_path}.") from exc

        if not data or file_not_found:
            if file_path == self.DEFAULT_SETTINGS_PATH:
                raise ValueError(f"No data in default game state file or not found: {file_path}")
            print(f"No data in game state file or file not found: {file_path}. \
Using default game state file.")
            self.__load_from_file(self.DEFAULT_SETTINGS_PATH)
        else:
            self.from_json(data)

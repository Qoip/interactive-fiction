'''Module containing GameSettings class.'''

from typing import Dict, Any


class GameSettings:
    '''Game settings container.'''

    def __init__(self):
        self.history_length: int
        self.context_messages: int
        self.assistant_instruction: str

    def from_json(self, json: Dict[str, Any]):
        '''Inits game settings from json object'''
        try:
            self.history_length = json["history_length"]
            self.context_messages = json["context_messages"]
            self.assistant_instruction = json["assistant_instruction"]
        except KeyError as exc:
            raise KeyError(f"JSON decode error:\n{json}") from exc

    def to_json(self) -> Dict[str, Any]:
        '''Makes json object from whole container'''
        return {
            "history_length": self.history_length,
            "context_messages": self.context_messages,
            "assistant_instruction": self.assistant_instruction
        }

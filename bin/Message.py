'''Module containing WebUI class.'''

from datetime import datetime
from typing import Dict, Any


class Message:
    '''OpenAI message container.'''

    def __init__(self, sender: str, message: str):
        self.sender = sender
        self.message = message
        self.timestamp = datetime.now()

    def __str__(self) -> str:
        '''Convert the message to a string representation.'''
        return f"{self.sender}: {self.message}"

    def is_empty(self) -> bool:
        '''Check for message emptiness.'''
        return self.message.strip() == ""

    def format(self) -> str:
        '''Format the message with timestamp and sender.'''
        return f'{self.timestamp} | {self.timestamp}: {self.message}'

    def to_json(self) -> Dict[str, Any]:
        '''Makes json object from class data'''
        return {
            "sender": self.sender,
            "message": self.message,
            "timestamp": self.timestamp.isoformat()
        }

    def from_json(self, json: Dict[str, Any]):
        '''Load message from json object'''
        try:
            self.sender = json["sender"]
            self.sender = json["message"]
            self.timestamp = datetime.fromisoformat(json["timestamp"])
        except KeyError as exc:
            raise KeyError(f"JSON decode error:\n{json}") from exc

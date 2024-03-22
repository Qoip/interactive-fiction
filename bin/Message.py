'''Module containing WebUI class.'''

from datetime import datetime


class Message:
    '''OpenAI message container.'''

    def __init__(self, sender: str, message: str, timestamp : datetime):
        self.sender = sender
        self.message = message
        self.timestamp = timestamp

    def is_empty(self) -> bool:
        '''Check for message emptiness.'''
        return self.message.strip() == ""

    def format(self):
        '''Format the message with timestamp and sender.'''
        return f'{self.timestamp} | {self.timestamp}: {self.message}'

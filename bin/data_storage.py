'''Module containing DataStorage class.'''

from message import Message
import os


class DataStorage:
    '''Saves logs.'''

    def message_log(self, message: Message):
        '''Log message.'''
        log_path = './data/log.log'
        with open(log_path, 'a') as file:
            file.write(message.format() + '\n')

    def reset(self):
        '''Reset data.'''
        file_path = './data/location.png'
        if os.path.exists(file_path):
            os.remove(file_path)

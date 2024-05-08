'''Module containing DataStorage class.'''

from message import Message


class DataStorage:
    '''Saves logs.'''

    def message_log(self, message: Message):
        '''Log message.'''
        log_path = './data/log.log'
        with open(log_path, 'a') as file:
            file.write(message.format() + '\n')

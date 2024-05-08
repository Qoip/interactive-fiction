'''Module containing DataStorage class.'''

from typing import List, Dict, Any  # delete Any
from message import Message
import os
import json


class DataStorage:
    '''Provides and saves to files category elements needed for storyline.'''

    def reset(self):
        '''Clear game storage.'''
        folder_path = './data/storage'
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)

    def get_category_list(self, category: str) -> List[str]:
        '''Returns list of available elements in category.'''
        folder_path = f'./data/storage/{category}'
        file_names = [filename for filename in os.listdir(folder_path)
                      if os.path.isfile(os.path.join(folder_path, filename))]
        return file_names

    def get_element(self, category: str, name: str) -> Dict[str, Any]:
        '''Returns element by name and category.'''
        file_path = f'./data/storage/{category}/{name}.json'
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        return {}

    def add_element(self, category: str, name: str, element: Dict[str, Any]):
        '''Adds element to category.'''
        category_path = f'./data/storage/{category}'
        if not os.path.exists(category_path):
            os.makedirs(category_path)
        element_path = f'{category_path}/{name}.json'
        with open(element_path, 'w') as file:
            json.dump(element, file)

    def message_log(self, message: Message):
        '''Log message.'''
        log_path = './data/storage/log.log'
        with open(log_path, 'a') as file:
            file.write(message.format() + '\n')

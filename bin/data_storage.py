'''Module containing DataStorage class.'''

from typing import List, Dict, Any  # delete Any
from message import Message


class DataStorage:
    '''Provides and saves to files category elements needed for storyline.'''

    def reset(self):
        '''Clear game storage.'''

    def get_category_list(self, category: str) -> List[str]:
        '''Returns list of available elements in category.'''

    def get_element(self, category: str, name: str) -> Dict[str, Any]:
        '''Returns element by name and category.'''

    def add_element(self, category: str, name: str, element: Dict[str, Any]):
        '''Adds element to category.'''

    def message_log(self, message: Message):
        '''Log message to db.'''

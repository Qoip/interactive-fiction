from typing import List, Any # delete Any
from bin.Message import Message

class DataStorage:
  '''
  Provides and saves to files category elements needed for storyline
  '''

  def Reset(self):
    '''
    Clear game storage
    '''
    pass

  def GetCategoryList(self, category : str) -> List[str]:
    '''
    Get list of available elements in category
    '''
    pass

  def GetElement(self, category : str, name : str) -> Any: # json!
    '''
    Get element  by category and name    
    '''
    pass

  def AddElement(self, category : str, name : str, element : Any): # json!
    '''
    Add element to category
    '''
    pass

  def MessageLog(self, message : Message):
    '''
    Log message to db
    '''
    pass
from bin.GameState import GameState
from bin.ContentGenerator import ContentGenerator
from bin.DataStorage import DataStorage
from bin.GameSettings import GameSettings

class GameEngine:

  state = GameState()
  __storage = DataStorage()
  __content_generator = ContentGenerator()

  def UserQuery(self, message : str):
    '''
    Resolve user game query
    '''
    pass
  
  def ResetState(self):
    '''
    Reset game
    '''
    pass

  def ChangeSettings(self, settings : GameSettings):
    '''
    Update settings
    '''
    pass

  def ChangeCategoryElement(self, category : str):
    '''
    Change current element by category
    '''
    pass
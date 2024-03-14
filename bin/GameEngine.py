from GameState import GameState
from ContentGenerator import ContentGenerator
from DataStorage import DataStorage
from GameSettings import GameSettings

class GameEngine:
  '''
  Main game manager
  '''

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
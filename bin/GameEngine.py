from GameState import GameState
from ContentGenerator import ContentGenerator
from DataStorage import DataStorage

class GameEngine:
  state = GameState()
  __storage = DataStorage()
  __content_generator = ContentGenerator()

  def UserQuery(self, message : str):
    pass
  
  def ResetState(self):
    pass

  def ChangeSettings(self):
    pass

  def ChangeCategoryElement(self):
    pass
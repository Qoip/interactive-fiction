from GameEngine import GameEngine
from GameSettings import GameSettings

class WebUI:
  def __init__(self):
    self.__game = GameEngine()
    self.__game_settings : GameSettings # GameSettings link

  def UserQueryListener(self):
    pass
  
  def ResetListener(self):
    pass

  def SettingsChangeListener(self):
    pass
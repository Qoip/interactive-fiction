from GameEngine import GameEngine
from GameSettings import GameSettings

class WebUI:
  '''
  Provides user interface to game and starts game
  Site server
  '''

  def __init__(self):
    self.__game = GameEngine()
    self.__game_settings : GameSettings # GameSettings link

  def UserQueryListener(self):
    '''
    Listener for user send query
    '''
    pass
  
  def ResetListener(self):
    '''
    Reset button listener
    '''
    pass

  def SettingsChangeListener(self):
    '''
    Settings change listener
    '''
    pass

if __name__ == '__main__':
  WebUI()
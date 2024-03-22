from typing import List, Any # delete Any
from GameSettings import GameSettings
from Message import Message

class GameState:
  '''
  Class responds to saving game current state
  '''

  _game_settings : GameSettings
  __last_messages : List[Message]
  __system_context : List[Message]
  __bars_info : Any # json!

  def GetContextMessages() -> List[Message]:
    '''
    Return message for query context
    '''
    pass
  
  def AddMessage(message : Message):
    '''
    Add message to message history
    '''
    pass

  def GetSystemContext() -> List[Message]:
    '''
    Return system context messages
    '''
    pass

  def AddSystemContext(message : Message):
    '''
    Add message to system context messages
    '''
    pass

  def GetBars() -> Any: # json object!
    '''
    Return bars information
    '''
    pass

  def SetBars(bars_info):
    '''
    Update bars
    '''
    pass

  def Reset():
    '''
    Reset all information to clear game
    '''
    pass

  def SetGameSettings(settings : GameSettings):
    '''
    Update game settings
    '''
    pass

  def __SaveToFile():
    '''
    Save state to file
    '''
    pass

  def __LoadFromFile():
    '''
    Load state from file
    '''
    pass

from typing import List, Any # delete Any
from GameSettings import GameSettings
from bin.Message import Message

class GameState:
  __game_settings : GameSettings
  __last_messages : List[Message]
  __system_context : List[Message]
  __bars_info : Any # json!

  def __init__(self):
    pass
  
  def GetContextMessages() -> List[Message]:
    pass
  
  def AddMessage(message : Message):
    pass

  def GetSystemContext() -> List[Message]:
    pass

  def AddSystemContext(message : Message):
    pass

  def GetBars() -> Any: # json object!
    pass

  def SetBars(bars_info):
    pass

  def Reset():
    pass

  def SetGameSettings(settings : GameSettings):
    pass

  def SaveToFile():
    pass

  def LoadFromFile():
    pass

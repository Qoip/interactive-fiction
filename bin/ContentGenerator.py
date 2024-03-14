from bin.Message import Message
from bin.GameState import GameState

class ContentGenerator:
  '''
  Provides API for resolving game queries
  '''
  
  __game_state : GameState # GameState link!

  def UserQuery(self, user_message : str) -> Message:
    '''
    Query to chatGPT from user
    '''
    pass

  def SystemQuery(self, system_message : str) -> Message:
    '''
    Query from system not for user
    '''
    pass

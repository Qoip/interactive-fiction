from bin.Message import Message
from GameState import GameState

class ContentGenerator:
  __game_state : GameState # GameState link

  def UserQuery(self, user_message : str) -> Message:
    pass

  def SystemQuery(self, system_message : str) -> Message:
    pass

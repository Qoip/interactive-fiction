class GameSettings:
  '''
  Game settings container
  '''

  def __init__(self, message_history_length = 5, context_messages = 5, assistant_instruction = ""):
    self.message_history_length = message_history_length
    self.context_messages = context_messages
    self.assistant_instruction = assistant_instruction
  
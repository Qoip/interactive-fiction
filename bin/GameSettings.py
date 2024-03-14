class GameSettings:
  def __init__(self, message_history_length, context_messages, assistant_instruction):
    self.message_hystory_length = message_history_length
    self.context_messages = context_messages
    self.assistant_instruction = assistant_instruction
  
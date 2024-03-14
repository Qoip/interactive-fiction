class Message:
  '''
  OpenAI message container
  '''
  def __init__(self, sender: str, message: str):
    self.sender = sender
    self.message = message

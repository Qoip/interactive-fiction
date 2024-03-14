from typing import Any # delete
from Message import Message

class DataStorage:

  def Reset():
    pass

  def GetCategoryList(category : str):
    pass

  def GetElement(category : str, name : str) -> Any: # json!
    pass

  def AddElement(category : str, name : str, element : Any): # json!
    pass

  def MessageLog(message : Message):
    pass
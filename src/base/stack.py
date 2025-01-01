from typing import Any

class Stack:
  def __init__(self):
    self.__storage = []

  def empty(self):
    return self.size() == 0

  def size(self):
    return len(self.__storage)
  
  def push(self, value : Any):
    self.__storage.append(value)

  def pop(self):
    if self.empty():
      raise IndexError("Ngăn xếp rỗng")
    return self.__storage.pop()    
    
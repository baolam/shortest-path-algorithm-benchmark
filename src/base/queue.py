from typing import Any
from collections import deque

class Queue:
  ### Cài đặt dựa trên deque (thư viện có sẵn hoạt động linh hoạt trong python)

  def __init__(self):
    self.__storage = deque()
  
  def size(self):
    return len(self.__storage)
  
  def empty(self):
    return self.size() == 0
  
  def push(self, item : Any):
    self.__storage.append(item)

  def pop(self):
    if self.empty():
      raise IndexError("Hàng đợi rỗng")
    return self.__storage.popleft()
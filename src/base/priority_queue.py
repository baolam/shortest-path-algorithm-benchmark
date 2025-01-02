from typing import Any
import heapq

class PriorityQueue:
  def __init__(self):
    self.__storage = []

  def size(self):
    return len(self.__storage)
  
  def empty(self):
    return len(self.__storage) == 0
  
  def push(self, item : Any, score : int | float):
    heapq.heappush(self.__storage, (score, (score, item)))
  
  def pop(self):
    if self.empty():
      raise IndexError("Hàng đợi ưu tiên rỗng")
    return heapq.heappop(self.__storage)[1]
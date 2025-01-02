import math
from typing import List

from ..base.visit import get_possible_move
from ..base.stack import Stack

def dfs_exist_path(size, position, matrix):
  start, end = position
  visited = [[False for _ in range(size)] for _ in range(size)]

  stack = Stack()
  stack.push(start)

  while not stack.empty():
    current = stack.pop()

    x, y = current
    visited[x][y] = True

    if current == end:
      return True
    
    for move in get_possible_move(x, y, matrix):
      if not visited[move[0]][move[1]]:
        stack.push(move)
        visited[move[0]][move[1]] = True

  return False

def dfs_shortest_path(size, position, matrix):
  start, end = position
  visited = [[False for _ in range(size)] for _ in range(size)]
  shortest_path = None

  stack = Stack()
  stack.push((start, [start]))

  while not stack.empty():
    current, path = stack.pop()

    visited[current[0]][current[1]] = True
    
    if current == end:
      if shortest_path is None or len(path) < len(shortest_path):
        shortest_path = path
      continue

    for move in get_possible_move(current[0], current[1], matrix):
      if not visited[move[0]][move[1]]:
        stack.push((move, path + [move]))
        visited[move[0]][move[1]] = True

  
  return shortest_path
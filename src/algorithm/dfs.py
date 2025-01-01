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
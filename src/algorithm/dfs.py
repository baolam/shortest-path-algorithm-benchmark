import math

from ..base.visit import get_possible_move, get_visited_matrix
from ..base.stack import Stack

def dfs_exist_path(size, position, matrix):
  start, end = position
  visited = get_visited_matrix(size)

  stack = Stack()
  stack.push(start)

  while not stack.empty():
    current = stack.pop()

    if current == end:
      return True
    
    x, y = current
    if visited[x][y]:
      continue
    visited[x][y] = True

    for move in get_possible_move(x, y, matrix):
      if not visited[move[0]][move[1]]:
        stack.push(move)

  return False

def dfs_shortest_path_exist_path(size, position, matrix):
  # Hàm cài đặt thuật toán DFS cho việc kiếm đường đi ngắn nhất trong bộ test exist_path
  start, end = position
  visited = get_visited_matrix(size)
  shortest_path = None

  stack = Stack()
  stack.push((start, [start]))

  while not stack.empty():
    current, path = stack.pop()
    
    if current == end:
      if shortest_path is None or len(path) < len(shortest_path):
        shortest_path = path
      continue
    
    x, y = current
    if visited[x][y]:
      continue
    visited[x][y] = True

    for move in get_possible_move(current[0], current[1], matrix):
      if not visited[move[0]][move[1]]:
        stack.push((move, path + [move]))

  return shortest_path

def dfs_shortest_path(size, position, matrix):
  start, end = position
  visited = get_visited_matrix(size)

  best_cost = math.inf
  best_path = []

  stack = Stack()
  stack.push((0, [start]))

  while not stack.empty():
    distance, path = stack.pop()
    current = path[-1]

    if current == end:
      if distance < best_cost:
        best_cost = distance
        best_path = path
      continue

    x, y = current
    if visited[x][y]:
      continue
    visited[x][y] = True

    for move in get_possible_move(x, y, matrix):
      if not visited[move[0]][move[1]]:
        stack.push((distance + matrix[move[0]][move[1]], path + [move]))

  return best_path
import math

from ..base.visit import get_possible_move, get_visited_matrix
from ..base.queue import Queue

def bfs_exist_path(size, position, matrix):
  # Thuật toán BFS dành cho việc có hay không có đường đi từ start tới end trong position
  start, end = position
  visited = get_visited_matrix(size)
  
  queue = Queue()
  queue.push(start)

  while not queue.empty():
    current = queue.pop()

    if current == end:
      return True
        
    x, y = current
    if visited[x][y]:
      continue
    visited[x][y] = True

    for move in get_possible_move(x, y, matrix):
      if not visited[move[0]][move[1]]:
        queue.push((move[0], move[1]))

  return False


def bfs_shortest_path_exist_path(size, position, matrix):
  # Hàm cài đặt thuật toán BFS cho việc kiếm đường đi ngắn nhất trong bộ test exist_path
  start, end = position
  visited = get_visited_matrix(size)
  
  queue = Queue()
  queue.push([start])

  while not queue.empty():
    path = queue.pop()
    current = path[-1]

    if current == end:
      return path
    
    x, y = current
    if visited[x][y]:
      continue
    visited[x][y] = True

    for move in get_possible_move(current[0], current[1], matrix):
      if not visited[move[0]][move[1]]:
        queue.push(path + [move])

  return []

def bfs_shortest_path(size, position, matrix):
  # Hàm cài đặt thuật toán BFS cho việc kiếm đường đi ngắn nhất trong bộ test shortest_path_maze
  start, end = position
  visited = get_visited_matrix(size)

  best_cost = math.inf
  best_path = []

  queue = Queue()
  queue.push((0, [start]))

  while not queue.empty():
    cost, path = queue.pop()
    current = path[-1]

    if current == end:
      if cost < best_cost:
        best_cost = cost
        best_path = path
      continue

    x, y = current
    if visited[x][y]:
      continue
    visited[x][y] = True

    for move in get_possible_move(x, y, matrix):
      if not visited[move[0]][move[1]]:
        queue.push((cost + matrix[move[0]][move[1]], path + [move]))

  return best_path
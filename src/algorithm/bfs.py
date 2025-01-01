from ..base.visit import get_possible_move
from ..base.queue import Queue

def bfs_exist_path(size, position, matrix):
  # Thuật toán BFS dành cho việc có hay không có đường đi từ start tới end trong position
  start, end = position
  visited = [[False for _ in range(size)] for _ in range(size)]
  
  queue = Queue()
  queue.push(start)

  while not queue.empty():
    current = queue.pop()

    x, y = current

    visited[x][y] = True

    if current == end:
      return True
    
    for move in get_possible_move(x, y, matrix):
      if not visited[move[0]][move[1]]:
        queue.push((move[0], move[1]))
        visited[move[0]][move[1]] = True

  return False


def bfs_shortest_path(size, position, matrix):
  pass
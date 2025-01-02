import math

from ..base.visit import get_possible_move
from ..base.priority_queue import PriorityQueue

def dijkstra_shortest_path(size, position, matrix):
  start, end = position
  visited = [[False for _ in range(size)] for _ in range(size)]

  priority_queue = PriorityQueue()
  priority_queue.push((0, [start]))

  while not priority_queue.empty():
    score, path = priority_queue.pop()
    current = path[-1]

    if current == end:
      return score, path
    
    x, y = current
    if visited[x][y]:
      continue
    visited[x][y] = True

    for move in get_possible_move(x, y, matrix):
      if not visited[move[0]][move[1]]:
        new_score = score + matrix[move[0]][move[1]]
        priority_queue.push((new_score, path + [move]))

  return math.inf, []
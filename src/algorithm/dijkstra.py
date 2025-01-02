import math

from ..base.visit import get_possible_move
from ..base.priority_queue import PriorityQueue

def dijkstra_shortest_path(size, position, matrix):
  start, end = position
  visited = [[False for _ in range(size)] for _ in range(size)]
  distance = [[0] * size for _ in range(size)]

  priority_queue = PriorityQueue()
  priority_queue.push([start], 0)

  while not priority_queue.empty():
    current_distance, path = priority_queue.pop()
    current = path[-1]

    if current == end:
      return current_distance, path
    
    x, y = current
    if visited[x][y]:
      continue
    visited[x][y] = True

    for move in get_possible_move(x, y, matrix):
      new_distance = current_distance + matrix[move[0]][move[1]]
      
      if not visited[move[0]][move[1]] or new_distance < distance[move[0]][move[1]]:
        distance[move[0]][move[1]] = new_distance
        priority_queue.push(path + [move], new_distance)

  return math.inf, []
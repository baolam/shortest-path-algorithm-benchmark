import math

from ..base.visit import get_possible_move, get_visited_matrix
from ..base.priority_queue import PriorityQueue

def _eucclid_distance(current, end):
  start_x, start_y = current
  end_x, end_y = current
  return ((end_x - start_x) ** 2 + (end_y - start_y) ** 2) ** 0.5

def _mahatan_distance(current, end):
  start_x, start_y = current
  end_x, end_y = end
  return math.abs(end_x - start_x) + math.abs(end_y - start_y)

def a_star_shortest_path(size, position, matrix, heuristic):
  start, end = position
  visited = get_visited_matrix(size)

  priority_queue = PriorityQueue()
  priority_queue.push((heuristic(start, end), start, []))

  while not priority_queue.empty():
    current_distance, current, path = priority_queue.pop()

    if current == end:
      return current_distance, path
    
    x, y = current
    if visited[x][y]:
      continue
    visited[x][y] = True

    for move in get_possible_move(x, y, matrix):
      if not visited[move[0]][move[1]]:
        score = current_distance + heuristic(move, end)
        priority_queue.push((score, move, path + [move]))

  return math.inf, []

def a_star_euclid_heuristic(size, position, matrix):
  return a_star_shortest_path(size, position, matrix, _eucclid_distance)

def a_star_mahatan_heuristic(size, position, matrix):
  return a_star_shortest_path(size, position, matrix, _mahatan_distance)
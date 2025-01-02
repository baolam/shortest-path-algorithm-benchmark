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
  return abs(end_x - start_x) + abs(end_y - start_y)

def a_star_shortest_path(size, position, matrix, heuristic):
  start, end = position
  visited = get_visited_matrix(size)
  g_scores = [[0] * size for _ in range(size)]

  priority_queue = PriorityQueue()
  priority_queue.push([start], heuristic(start, end))

  while not priority_queue.empty():
    __, path = priority_queue.pop()
    current = path[-1]

    if current == end:
      return g_scores[current[0]][current[1]], path
    
    x, y = current
    if visited[x][y]:
      continue
    visited[x][y] = True

    for move in get_possible_move(x, y, matrix):
      tentative_g = g_scores[x][y] + matrix[move[0]][move[1]]

      if not visited[move[0]][move[1]] or tentative_g < g_scores[move[0]][move[1]]:
        g_scores[move[0]][move[1]] = tentative_g
        f_score = tentative_g + heuristic(move, end)

        priority_queue.push(path + [move], f_score)

  return math.inf, []

def a_star_euclid_heuristic(size, position, matrix):
  return a_star_shortest_path(size, position, matrix, _eucclid_distance)

def a_star_mahatan_heuristic(size, position, matrix):
  return a_star_shortest_path(size, position, matrix, _mahatan_distance)
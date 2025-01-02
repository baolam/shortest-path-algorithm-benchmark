from ..constant import DIRECTIONS, CAN_NOT_WALK

def get_possible_move(x, y, matrix):
  # Trả về các bước đi tiềm năng trong thuật toán
  
  size = len(matrix)
  possible_move = []
  
  for direction in DIRECTIONS:
    new_x, new_y = x + direction[0], y + direction[1]
    
    if not (0 <= new_x < size and 0 <= new_y < size):
      continue
    if matrix[new_x][new_y] == CAN_NOT_WALK:
      continue

    possible_move.append((new_x, new_y))
  
  return possible_move


def get_visited_matrix(size):
  return [[False for _ in range(size)] for _ in range(size)]
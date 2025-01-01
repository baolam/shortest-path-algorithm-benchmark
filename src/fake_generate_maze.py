import random
from .constant import *

def _generate_size():
  # Hàm sinh kích thước mê cung
  return random.randint(MIN_SIZE, MAX_SIZE)

def __generate_pos(size):
  return random.randint(0, size - 1)

def _generate_barrier(size, portion_barrier : int = PORTION_BARRIER):
  # Hàm sinh các vật cản của mê cung
  num_barrier = int(size * size * portion_barrier)
  _barrier = [[0] * size for _ in range(size)]

  for _ in range(num_barrier):
    x, y = __generate_pos(size), __generate_pos(size)
    _barrier[x][y] = 1
  
  return _barrier

def _generate_weights(barrier_matrix):
  # Hàm sinh trọng số của các ô trong mê cung
  size = len(barrier_matrix)
  weights = [[CAN_NOT_WALK] * size for _ in range(size)]
  
  for i in range(size):
    for j in range(size):
      if not barrier_matrix[i][j]:
        weights[i][j] = random.randint(MIN_WEIGHT, MAX_WEIGHT)

  return weights

def _generate_position(size, barrier):
  # Hàm sinh vị trí xuất phát và đích
  start_x, start_y = __generate_pos(size), __generate_pos(size)
  end_x, end_y = __generate_pos(size), __generate_pos(size)

  while (start_x, start_y) >= (end_x, end_y):
    start_x, start_y = __generate_pos(size), __generate_pos(size)
    end_x, end_y = __generate_pos(size), __generate_pos(size)

    while barrier[start_x][start_y]:
      start_x, start_y = __generate_pos(size), __generate_pos(size)
      
    while barrier[end_x][end_y]:
      end_x, end_y = __generate_pos(size), __generate_pos(size)

  return (start_x, start_y), (end_x, end_y)

def generate_test(weightable : bool = False):
  # Hàm sinh dữ liệu thử nghiệm
  size = _generate_size()
  weights = _generate_barrier(size)
  position = _generate_position(size, weights)

  if weightable:
    weights = _generate_weights(weights)

  return size, position, weights
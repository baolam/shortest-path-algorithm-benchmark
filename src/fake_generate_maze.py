import random
from .constant import *

def _generate_size():
  # Hàm sinh kích thước mê cung
  return random.randint(MIN_SIZE, MAX_SIZE)

def _generate_barrier(size, portion_barrier : int = PORTION_BARRIER):
  # Hàm sinh các vật cản của mê cung
  num_barrier = int(size * size * portion_barrier)
  _barrier = [[0] * size for _ in range(size)]

  for _ in range(num_barrier):
    x, y = random.randint(0, size - 1), random.randint(0, size - 1)
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

def _generate_position(size):
  # Hàm sinh vị trí xuất phát và đích
  start_x, start_y = random.randint(0, size - 1), random.randint(0, size - 1)
  end_x, end_y = random.randint(0, size - 1), random.randint(0, size - 1)
  while (start_x, start_y) >= (end_x, end_y):
    end_x, end_y = random.randint(0, size - 1), random.randint(0, size - 1)
  return (start_x, start_y), (end_x, end_y)

def generate_test(weightable : bool = False):
  # Hàm sinh dữ liệu thử nghiệm
  size = _generate_size()
  position = _generate_position(size)
  weights = _generate_barrier(size)

  if weightable:
    weights = _generate_weights(weights)

  return size, position, weights
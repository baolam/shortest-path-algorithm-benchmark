import os

from .constant import *

root_folder = FOLDER_TEST
if not os.path.exists(root_folder):
  raise ValueError(f"Không có thư mục lưu trữ bộ dữ liệu: {root_folder}")

def read_test(test_name : str):
  # Đọc dữ liệu test đầu vào để áp dụng thuật toán
  # test_folder: thư mục chứa dữ liệu test
  _test_folder = os.path.join(root_folder, test_name)
  if not os.path.exists(_test_folder):
    raise ValueError(f"Không có thư mục lưu trữ dữ liệu test: {_test_folder}")
  input_file = os.path.join(_test_folder, "input.txt")
  
  f = open(input_file, "r", encoding="utf-8")
  size = int(f.readline())
  start_x, start_y, end_x, end_y = map(int, f.readline().split())

  matrix = []
  for i in range(size):
    row = list(map(int, f.readline().split()))
    matrix.append(row)

  f.close()

  return size, ((start_x, start_y), (end_x, end_y)), matrix

def write_test(test_name : str, size, position, matrix):
  # Ghi dữ liệu test đầu ra
  # test_folder: thư mục chứa dữ liệu test
  _test_folder = os.path.join(root_folder, test_name)
  if not os.path.exists(_test_folder):
    os.makedirs(_test_folder)
  output_file = os.path.join(_test_folder, "input.txt")

  f = open(output_file, "w", encoding="utf-8")
  start_x, start_y = position[0]
  end_x, end_y = position[1]
  
  f.write(str(size) + "\n")
  f.write(str(start_x) + " " + str(start_y) + " " + str(end_x) + " " + str(end_y))
  f.write("\n")

  for row in matrix:
    f.write(" ".join(map(str, row)) + "\n")
  
  f.close()

def write_test_without_test_name(size, position, matrix):
  # Ghi dữ liệu test đầu ra
  # test_folder: thư mục chứa dữ liệu test

  num_tests = len(os.listdir(root_folder))
  test_name = "test_" + str(num_tests + 1)

  return write_test(test_name, size, position, matrix)
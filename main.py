from src.algorithm.bfs import bfs_exist_path
from src.data import read_test

size, position, matrix = read_test("test_1")
print(bfs_exist_path(size, position, matrix))
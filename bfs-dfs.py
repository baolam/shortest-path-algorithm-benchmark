import cProfile
import pstats

from src.algorithm.bfs import bfs_exist_path
from src.algorithm.dfs import dfs_exist_path
from src.data import read_test, get_tests

tests = [read_test(test) for test in get_tests()]

def _evaluate(algorithm):
  for size, position, matrix in tests:
    algorithm(size, position, matrix)

def bfs_evaluate():
  _evaluate(bfs_exist_path)

def dfs_evaluate():
  _evaluate(dfs_exist_path)

def main():
  bfs_evaluate()
  dfs_evaluate()

if __name__ == "__main__":
  cProfile.run('main()', 'bfs-dfs-comparison.prof')
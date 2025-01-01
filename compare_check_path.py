import cProfile
import pstats

from src.algorithm.bfs import bfs_exist_path
from src.algorithm.dfs import dfs_exist_path
from src.data import read_test, get_tests

criteria = "exist_path"
tests = [read_test(test) for test in get_tests()]

def _evaluate(algorithm):
  for size, position, matrix in tests:
    algorithm(size, position, matrix)


def main():
  _evaluate(bfs_exist_path)
  _evaluate(dfs_exist_path)
  
if __name__ == "__main__":
  cProfile.run('main()', 'results/exist_path.prof')
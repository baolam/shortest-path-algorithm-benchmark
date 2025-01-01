import cProfile

from src.algorithm.bfs import bfs_exist_path
from src.algorithm.dfs import dfs_exist_path
from src import pattern_comparison

_evaluate = pattern_comparison("exist_path")

def main():
  _evaluate(bfs_exist_path)
  _evaluate(dfs_exist_path)
  
if __name__ == "__main__":
  cProfile.run('main()', 'results/exist_path.prof')
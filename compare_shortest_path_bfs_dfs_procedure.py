import cProfile

from src.algorithm.bfs import bfs_shortest_path
from src.algorithm.dfs import dfs_shortest_path
from src import pattern_comparison

criteria = "exist_path"
_evaluate = pattern_comparison(criteria)

def main():
  _evaluate(bfs_shortest_path)
  _evaluate(dfs_shortest_path)

if __name__ == "__main__":
  cProfile.run('main()', 'results/exist_path_bfs_dfs_for_shortest_path.prof')
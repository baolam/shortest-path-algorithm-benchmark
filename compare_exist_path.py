import cProfile

from src.algorithm.bfs import bfs_shortest_path
from src.algorithm.dfs import dfs_shortest_path
from src.algorithm.a_star import a_star_mahatan_heuristic
from src.algorithm.dijkstra import dijkstra_shortest_path
from src import pattern_comparison

criteria = "exist_path"
_evaluate = pattern_comparison(criteria)

def main():
  _evaluate(bfs_shortest_path)
  _evaluate(dfs_shortest_path)
  _evaluate(dijkstra_shortest_path)
  _evaluate(a_star_mahatan_heuristic)

if __name__ == "__main__":
  cProfile.run("main()", "results/matrix_without_weight.prof")
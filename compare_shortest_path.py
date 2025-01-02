import cProfile

from src.algorithm.bfs import bfs_shortest_path
from src.algorithm.dfs import dfs_shortest_path
from src.algorithm.dijkstra import dijkstra_shortest_path
from src.algorithm.a_star import a_star_mahatan_heuristic, a_star_euclid_heuristic
from src import pattern_comparison

criteria = "shortest_path_maze"
_evaluate = pattern_comparison(criteria)

def euclid():
  _evaluate(a_star_euclid_heuristic)

def mahatan():
  _evaluate(a_star_mahatan_heuristic)

def main():
  _evaluate(bfs_shortest_path)
  _evaluate(dfs_shortest_path)
  _evaluate(dijkstra_shortest_path)
  euclid()
  mahatan()

if __name__ == "__main__":
  cProfile.run("main()", "results/matrix_with_weight.prof")
import cProfile

from src.algorithm.a_star import a_star_euclid_heuristic, a_star_mahatan_heuristic
from src import pattern_comparison

criteria = "exist_path"
_evaluate = pattern_comparison(criteria)

def euclid():
  _evaluate(a_star_euclid_heuristic)

def mahatan():
  _evaluate(a_star_mahatan_heuristic)

def main():
  euclid()
  mahatan()

if __name__ == "__main__":
  cProfile.run("main()", "results/a_star_heuristic.prof")
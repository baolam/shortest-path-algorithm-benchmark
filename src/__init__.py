from .data_folder_manager import read_test, get_tests

def pattern_comparison(criteria):
  tests = [ read_test(criteria, test_name) for test_name in get_tests(criteria) ]

  def execute(algorithm):
    for size, position, matrix in tests:
      algorithm(size, position, matrix)
  
  return execute
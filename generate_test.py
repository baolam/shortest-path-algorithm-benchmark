from tqdm import tqdm

from src.fake_generate_maze import generate_test
from src.data import write_test_without_test_name

num_test = 10

print("Đang tiến hành sinh test...")
for i in tqdm(range(1, num_test + 1)):
  size, position, matrix = generate_test(weightable=False)
  write_test_without_test_name(size, position, matrix)
print("Hoàn thành sinh test....")
from tqdm import tqdm

from src.fake_generate_maze import generate_test
from src.data import write_test_without_test_name

num_test = int(input("Hãy nhập số lượng test muốn sinh: "))
criteria = input("Hãy nhập tiêu chuẩn đánh giá bạn muốn sinh dữ liệu")
weightable = input("Có trọng số hay không?: Yes/No")
if weightable == "Yes":
  weightable = True
else:
  weightable = False

print("Đang tiến hành sinh test...")
for i in tqdm(range(1, num_test + 1)):
  size, position, matrix = generate_test(weightable=weightable)
  write_test_without_test_name(criteria, size, position, matrix)
print("Hoàn thành sinh test....")
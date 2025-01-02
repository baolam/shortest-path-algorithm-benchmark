# Benchmark thuật toán tìm đường đi ngắn nhất

## So sánh với những thuật toán:

- Thuật toán DFS
- Thuật toán BFS
- Thuật toán Dijkstra
- Thuật toán A\*

## Tiêu chí so sánh (dựa trên thời gian thực thi thuật toán)

- Vấn đề, kiểm tra sự tồn tại đường đi giữa hai vị trí được cho
- Vấn đề, kiểm tra đường đi ngắn nhất giữa hai vị trí được cho

## So sánh trên các bộ dữ liệu:

- Dựa trên bộ dữ liệu được cung cấp

* Là bộ dữ liệu về mê cung, với các thông tin như:

- Vị trí bắt đầu và kết thúc
- Kích thước của mê cung
- Các rào cản trong mê cung
- Các điểm thưởng trong mê cung

## Cấu trúc dự án

- `data/`

  - `(criteria)`
    - `test_1`
      - `input.txt`
    - ...
  - `...`

- `results/`

  - `images/`
  - ... prof : các file lưu trữ kết quả thực thi thuật toán

- `src/`

  - `algorithm/` : chứa mã cài đặt các thuật toán
  - `base/` : chứa mã cài đặt một số cấu trúc dữ liệu, hàm hỗ trợ phục vụ thuật toán

  - **constant.py** : file chứa những biến cài đặt cho toàn bộ chương trình
  - **data_folder_manager.py** : file chứa những hàm phục vụ quản lí bộ dữ liệu test
  - **fake_generate_maze.py** : file chứa chương trình sinh mê cung, phục vụ cho test
  - \***\*init**.py\*\* : file chứa một số hàm tiện ích

## Kết quả thực thi

- **a_star_heuristic.prof**
  File lưu trữ thống kê thời gian thực thi của thuật toán a_star với vấn đề kiểm tra sự tồn tại đường đi giữa hai vị trí được cho với các hàm heuristic khác nhau (ơ-clit với mahatan)
  - Theo kết quả thực thi, hàm mahatan hiệu quả hơn khi so với ơ-clit trong vấn đề này.
- **exist_path.prof**
  File lưu trữ thống kê thời gian thực thi của thuật toán BFS, DFS cho việc kiểm tra tồn tại đường đi giữa hai vị trí cho trước
  - Theo kết quả thực thi, DFS hiệu quả hơn so với BFS trong vấn đề này.
- **matrix_with_weight.prof**
  File lưu trữ thống kê thời gian thực thi của các thuật toán BFS, DFS, Dijkstra, A\* (mahatan, euclid) cho việc tìm đường đi ngắn nhất giữa hai vị trí cho trước trong mê cung có trọng số
  - Theo kết quả thực thi, thuật toán A\* (mahatan, euclid) hiệu quả hơn và mahatan hiệu quả hơn toàn bộ, tiếp đến là thuật toán Dijkstra, rồi tới BFS, cuối cùng là DFS.
- **matrix_without_weight.prof**
  File lưu trữ thống kê thời gian thực thi của các thuật toán BFS, DFS, Dijkstra, A\* (mahatan, euclid) cho việc tìm đường đi ngắn nhất giữa hai vị trí cho trước trong mê cung không trọng số
  - Theo kết quả thực thi, A\* (mahatan) hiệu quả nhất, tới BFS, DFS rùi tới cuối Dijkstra

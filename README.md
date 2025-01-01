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

- `src/`

  - `algorithm/` : chứa mã cài đặt các thuật toán
  - `base/` : chứa mã cài đặt một số cấu trúc dữ liệu, hàm hỗ trợ phục vụ thuật toán

  - **constant.py** : file chứa những biến cài đặt cho toàn bộ chương trình
  - **data_folder_manager.py** : file chứa những hàm phục vụ quản lí bộ dữ liệu test
  - **fake_generate_maze.py** : file chứa chương trình sinh mê cung, phục vụ cho test
  - \***\*init**.py\*\* : file chứa một số hàm tiện ích

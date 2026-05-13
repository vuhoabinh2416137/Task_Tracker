# Task Tracker CLI

Task Tracker là một ứng dụng Command Line Interface (CLI) đơn giản để giúp bạn theo dõi và quản lý công việc của mình. Bạn có thể sử dụng ứng dụng này để quản lý các công việc cần làm (todo), đang làm (in-progress) và đã hoàn thành (done).

## Tính năng

- Thêm công việc mới (Add a new task)
- Cập nhật nội dung công việc (Update a task)
- Xóa công việc (Delete a task)
- Đánh dấu công việc đang làm (Mark a task as in-progress)
- Đánh dấu công việc đã hoàn thành (Mark a task as done)
- Hiển thị danh sách công việc ở dạng bảng đẹp mắt (List all tasks, List by status: todo, in-progress, done)

## Cấu trúc dữ liệu

Dữ liệu sẽ được lưu trữ cục bộ dưới định dạng JSON trong file `task.json`. Mỗi task sẽ có các thuộc tính:
- `id`: Định danh duy nhất.
- `description`: Mô tả công việc.
- `status`: Trạng thái của công việc (`todo`, `in-progress`, `done`).
- `created_at`: Thời gian tạo.
- `updated_at`: Thời gian cập nhật gần nhất.

## Hướng dẫn cài đặt

1. Đảm bảo bạn đã cài đặt [Python 3](https://www.python.org/downloads/) trên máy của mình.
2. Clone repository này hoặc tải mã nguồn về máy:
   ```bash
   git clone https://github.com/vuhoabinh2416137/Task_Tracker
   cd Task_Tracker
   ```
3. (Trên Windows) Mở Command Prompt hoặc PowerShell tại thư mục `Task_Tracker`. Bạn có thể chạy lệnh thông qua file `task-cli.bat` có sẵn:
   ```cmd
   task-cli --help
   ```
   *Lưu ý: Để gõ `task-cli` ở bất kỳ thư mục nào trên terminal, bạn có thể thêm đường dẫn thư mục `Task_Tracker` vào biến môi trường `PATH` của Windows.*

## Cách sử dụng

### 1. Xem hướng dẫn

```bash
task-cli -h
# Hoặc
task-cli --help
```

### 2. Thêm một công việc mới

```bash
task-cli add "Mua thức ăn cho mèo"
task-cli add "Học lập trình Python"
```

### 3. Cập nhật một công việc

Chỉ định ID của công việc và mô tả mới:

```bash
task-cli update 1 "Mua thức ăn cho chó và mèo"
```

### 4. Xóa một công việc

```bash
task-cli delete 1
```

### 5. Đánh dấu công việc đang làm (In Progress)

```bash
task-cli mark-in-progress 2
```

### 6. Đánh dấu công việc đã hoàn thành (Done)

```bash
task-cli mark-done 2
```

### 7. Hiển thị danh sách công việc

- Hiển thị tất cả công việc:
  ```bash
  task-cli list
  ```
- Hiển thị công việc đã hoàn thành:
  ```bash
  task-cli list done
  ```
- Hiển thị công việc chưa làm (Todo):
  ```bash
  task-cli list todo
  ```
- Hiển thị công việc đang làm (In Progress):
  ```bash
  task-cli list in-progress
  ```

## Tác giả
Dự án được xây dựng phục vụ cho việc học tập và rèn luyện kỹ năng lập trình.

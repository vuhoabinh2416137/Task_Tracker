import sys
import json
import os
import argparse
from datetime import datetime

# Cấu hình encoding UTF-8 cho stdout trên Windows để in tiếng Việt không lỗi
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Lấy thư mục gốc chứa file main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, 'task.json')

class TaskTracker:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename) or os.stat(self.filename).st_size == 0:
            return []
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)

    def _get_current_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _find_task_index(self, task_id):
        for index, task in enumerate(self.tasks):
            if task["id"] == task_id:
                return index
        return -1

    def add_task(self, description):
        task_id = self.tasks[-1]["id"] + 1 if self.tasks else 1
        new_task = {
            "id": task_id,
            "description": description,
            "status": "todo",
            "created_at": self._get_current_time(),
            "updated_at": self._get_current_time()
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task added successfully (ID: {task_id})")

    def update_task(self, task_id, new_description):
        index = self._find_task_index(task_id)
        if index != -1:
            self.tasks[index]["description"] = new_description
            self.tasks[index]["updated_at"] = self._get_current_time()
            self.save_tasks()
            print(f"Task updated successfully (ID: {task_id})")
        else:
            print(f"Task not found (ID: {task_id})")

    def delete_task(self, task_id):
        index = self._find_task_index(task_id)
        if index != -1:
            del self.tasks[index]
            self.save_tasks()
            print(f"Task deleted successfully (ID: {task_id})")
        else:
            print(f"Task not found (ID: {task_id})")

    def change_status(self, task_id, new_status):
        index = self._find_task_index(task_id)
        if index != -1:
            self.tasks[index]["status"] = new_status
            self.tasks[index]["updated_at"] = self._get_current_time()
            self.save_tasks()
            print(f"Task marked as {new_status} successfully (ID: {task_id})")
        else:
            print(f"Task not found (ID: {task_id})")

    def list_tasks(self, status=None):
        filtered_tasks = [t for t in self.tasks if status is None or t["status"] == status]
        if not filtered_tasks:
            print("No tasks found.")
            return

        print(f"{'ID':<5} | {'Status':<12} | {'Created At':<20} | {'Updated At':<20} | {'Description'}")
        print("-" * 85)
        for task in filtered_tasks:
            # Xử lý tương thích ngược: lấy "updated_at" hoặc fallback về "update_at"
            updated_at = task.get("updated_at", task.get("update_at", ""))
            print(f"{task['id']:<5} | {task['status']:<12} | {task['created_at']:<20} | {updated_at:<20} | {task['description']}")


def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI - Công cụ quản lý công việc trên Terminal", prog="task-cli")
    subparsers = parser.add_subparsers(dest="command", help="Danh sách lệnh khả dụng")

    # Add command
    parser_add = subparsers.add_parser("add", help="Thêm một task mới")
    parser_add.add_argument("description", type=str, help="Mô tả công việc")

    # Update command
    parser_update = subparsers.add_parser("update", help="Cập nhật một task đã có")
    parser_update.add_argument("id", type=int, help="ID của task")
    parser_update.add_argument("description", type=str, help="Mô tả mới của công việc")

    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Xóa một task")
    parser_delete.add_argument("id", type=int, help="ID của task")

    # Mark In Progress command
    parser_mark_ip = subparsers.add_parser("mark-in-progress", help="Đánh dấu task đang được thực hiện (in-progress)")
    parser_mark_ip.add_argument("id", type=int, help="ID của task")

    # Mark Done command
    parser_mark_done = subparsers.add_parser("mark-done", help="Đánh dấu task đã hoàn thành (done)")
    parser_mark_done.add_argument("id", type=int, help="ID của task")

    # List command
    parser_list = subparsers.add_parser("list", help="Hiển thị danh sách các task")
    parser_list.add_argument("status", nargs="?", choices=["done", "todo", "in-progress"], help="Lọc task theo trạng thái (tuỳ chọn)")

    args = parser.parse_args()

    # Nếu không nhập lệnh nào, hiển thị help
    if not args.command:
        parser.print_help()
        sys.exit(1)

    tracker = TaskTracker(FILE_NAME)

    try:
        if args.command == "add":
            tracker.add_task(args.description)
        elif args.command == "update":
            tracker.update_task(args.id, args.description)
        elif args.command == "delete":
            tracker.delete_task(args.id)
        elif args.command == "mark-in-progress":
            tracker.change_status(args.id, "in-progress")
        elif args.command == "mark-done":
            tracker.change_status(args.id, "done")
        elif args.command == "list":
            tracker.list_tasks(args.status)
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    main()
import sys
import json
import os
from datetime import datetime

FILE_NAME = 'task.json'

# --- HÀM XỬ LÝ FILE ---
def load_tasks():
    """Đọc dữ liệu từ file JSON. Nếu file chưa có hoặc trống, trả về danh sách rỗng."""
    if not os.path.exists(FILE_NAME) or os.stat(FILE_NAME).st_size == 0:
        return []
    
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """Ghi danh sách tasks vào file JSON."""
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

# --- CÁC HÀM XỬ LÝ LOGIC CHÍNH ---
def add_task(description):
    tasks = load_tasks()
    if len(tasks) == 0:
        id = 1
    else:
        id = tasks[-1]["id"]  + 1

    new_task = {
        "id": id,
        "description": description,
        "status": "todo",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "update_at" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    } 
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {id}, Description: {description})")
def update_task(task_id, new_description):
    tasks = load_tasks()
    not_found = True
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["update_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            not_found = False
            break
    if not_found:
        print(f"Task not found (ID: {task_id})")
    else:
        save_tasks(tasks)
        print(f"Task updated successfully (ID: {task_id}, Description: {new_description})")
def delete_task(task_id):
    tasks  = load_tasks()
    not_found = True
    for task in tasks:
        if task["id"] == task_id:
            description = task["description"]
            tasks.remove(task)
            not_found = False
            break
    if not_found:
        print(f"Task not found (ID: {task_id})")
    else:
        save_tasks(tasks)
        print(f"Task deleted successfully (ID: {task_id}, Description: {description})") 

def mark_task_in_progress(task_id):
    tasks    = load_tasks()
    not_found = True
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            not_found = False
            break
    if not_found:
        print(f"Task not found (ID: {task_id})")
    else:
        save_tasks(tasks)
        print(f"Task marked as in-progress successfully (ID: {task_id})")

def mark_task_done(task_id):
    tasks = load_tasks()
    not_found = True
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            not_found = False
            break
    if not_found:
        print(f"Task not found (ID: {task_id})")
    else:
        save_tasks(tasks)
        print(f"Task marked as done successfully (ID: {task_id})")

def list_all_tasks():
    tasks = load_tasks()
    for task in tasks:
        print(f"ID: {task['id']}, \n Description: {task['description']}, \n Status: {task['status']}, \n Created at: {task['created_at']}, \n Updated at: {task['update_at']}")

def list_done_tasks():
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "done":
            print(f"ID: {task['id']}, \n Description: {task['description']}, \n Status: {task['status']}, \n Created at: {task['created_at']}, \n Updated at: {task['update_at']}")

def list_todo_tasks():
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "todo":
            print(f"ID: {task['id']}, \n Description: {task['description']}, \n Status: {task['status']}, \n Created at: {task['created_at']}, \n Updated at: {task['update_at']}")
    
def list_in_progress_tasks():
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "in-progress":
            print(f"ID: {task['id']}, \n Description: {task['description']}, \n Status: {task['status']}, \n Created at: {task['created_at']}, \n Updated at: {task['update_at']}")

# --- ENTRY POINT (Nơi nhận lệnh từ Terminal) ---
if __name__ == "__main__":
    # Nhận danh sách tham số từ Terminal (bỏ qua tên file main.py ở vị trí số 0)
    args = sys.argv[1:] 
    
    if len(args) == 0:
        print("Vui lòng nhập lệnh. Ví dụ: python main.py list")
    else:
        command = args[0]
        if command == "add":
            if len(args) < 2:
                print("Vui lòng nhập đầy đủ thông tin. Ví dụ: python main.py add \"buy groceries\"")
            else:
                description = " ".join(args[1:])
                add_task(description)
        elif command == "update":
            if len(args) < 3:
                print("Vui lòng nhập đẩy đủ thông tin. Ví dụ: pyhon main.py update 1 \"buy food\"")
            else:
                task_id = int(args[1]) # Chuyển đổi chuỗi thành số nguyên
                new_description = " ".join(args[2:])
                update_task(task_id, new_description)
        elif command == "delete":
            if len(args) < 2:
                print("Vui lòng nhập đẩy đủ thông tin. Ví dụ: pyhon main.py delete 1")
            else:
                task_id = int(args[1]) # Chuyển đổi chuỗi thành số nguyên
                delete_task(task_id)
        elif command == "mark-in-progress":
            if len(args) < 2:
                print("Vui lòng nhập đẩy đủ thông tin. Ví dụ: pyhon main.py mark-in-progress 1")
            else:
                task_id = int(args[1]) # Chuyển đổi chuỗi thành số nguyên
                mark_task_in_progress(task_id)
        elif command == "mark-done":
            if len(args) < 2:
                print("Vui lòng nhập đẩy đủ thông tin. Ví dụ: pyhon main.py mark-done 1")
            else:
                task_id = int(args[1]) # Chuyển đổi chuỗi thành số nguyên
                mark_task_done(task_id)
        elif command == "list":
            if len(args) == 1:
                list_all_tasks()
            elif args[1] == "done":
                list_done_tasks()
            elif args[1] == "todo":
                list_todo_tasks()
            elif args[1] == "in-progress":
                list_in_progress_tasks()
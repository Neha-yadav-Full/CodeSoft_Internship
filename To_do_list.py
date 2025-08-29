
"""
Simple CLI To-Do List with persistence (todo.json).
Features:
- Add task (description, optional priority, optional due date)
- List tasks (shows id, status, priority, due date)
- Update task description/priority/due date
- Mark task complete / incomplete
- Delete task
- Save / Load automatically from todo.json
"""

import json
import os
from datetime import datetime

DB_FILE = "todo.json"


def load_tasks():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_tasks(tasks):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def new_task_id(tasks):
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1


def add_task(tasks):
    desc = input("Task description: ").strip()
    if not desc:
        print("Description cannot be empty.")
        return
    priority = input("Priority (low/medium/high) [low]: ").strip().lower() or "low"
    due = input("Due date (YYYY-MM-DD) [optional]: ").strip()
    if due:
        try:
            datetime.strptime(due, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Skipping due date.")
            due = ""
    task = {
        "id": new_task_id(tasks),
        "description": desc,
        "priority": priority,
        "due": due,
        "done": False,
        "created_at": datetime.now().isoformat(),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task #{task['id']}")


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nTasks:")
    for t in sorted(tasks, key=lambda x: (x["done"], x["priority"], x["id"])):
        status = "✓" if t["done"] else " "
        due = f" | due: {t['due']}" if t["due"] else ""
        print(f"#{t['id']:>2} [{status}] {t['description']} (priority: {t['priority']}){due}")
    print()


def find_task(tasks, tid):
    for t in tasks:
        if t["id"] == tid:
            return t
    return None


def update_task(tasks):
    try:
        tid = int(input("Task id to update: ").strip())
    except ValueError:
        print("Invalid id.")
        return
    t = find_task(tasks, tid)
    if not t:
        print("Task not found.")
        return
    print("Leave blank to keep current value.")
    desc = input(f"Description [{t['description']}]: ").strip()
    if desc:
        t["description"] = desc
    priority = input(f"Priority [{t['priority']}]: ").strip().lower()
    if priority:
        t["priority"] = priority
    due = input(f"Due date [{t['due'] or 'none'}] (YYYY-MM-DD): ").strip()
    if due:
        try:
            datetime.strptime(due, "%Y-%m-%d")
            t["due"] = due
        except ValueError:
            print("Invalid date. Keeping old value.")
    save_tasks(tasks)
    print("Task updated.")


def mark_task(tasks, done=True):
    try:
        tid = int(input("Task id: ").strip())
    except ValueError:
        print("Invalid id.")
        return
    t = find_task(tasks, tid)
    if not t:
        print("Task not found.")
        return
    t["done"] = done
    save_tasks(tasks)
    print("Marked as done." if done else "Marked as not done.")


def delete_task(tasks):
    try:
        tid = int(input("Task id to delete: ").strip())
    except ValueError:
        print("Invalid id.")
        return
    t = find_task(tasks, tid)
    if not t:
        print("Task not found.")
        return
    tasks.remove(t)
    save_tasks(tasks)
    print("Task deleted.")


def clear_all(tasks):
    confirm = input("Delete ALL tasks? Type 'YES' to confirm: ")
    if confirm == "YES":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks deleted.")
    else:
        print("Aborted.")


def show_menu():
    print("""
To-Do List - Commands:
1) Add task
2) List tasks
3) Update task
4) Mark complete
5) Mark not complete
6) Delete task
7) Clear all tasks
0) Exit
""")


def main():
    tasks = load_tasks()
    while True:
        show_menu()
        cmd = input("Choose option: ").strip()
        if cmd == "1":
            add_task(tasks)
        elif cmd == "2":
            list_tasks(tasks)
        elif cmd == "3":
            update_task(tasks)
        elif cmd == "4":
            mark_task(tasks, True)
        elif cmd == "5":
            mark_task(tasks, False)
        elif cmd == "6":
            delete_task(tasks)
        elif cmd == "7":
            clear_all(tasks)
        elif cmd == "0":
            print("Bye.")
            break
        else:
            print("Unknown option.")


if __name__ == "__main__":
    main()



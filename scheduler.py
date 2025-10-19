# scheduler.py
from task import Task
import json
from datetime import datetime

class Scheduler:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, name, priority, deadline, duration):
        task = Task(name, priority, deadline, duration)
        self.tasks.append(task)
        self.save_tasks()

    def show_tasks(self):
        # Return tasks sorted
        return self.sort_tasks()

    def mark_completed(self, index):
        # index refers to the sorted list shown in the UI.
        sorted_tasks = self.sort_tasks()
        if 0 <= index < len(sorted_tasks):
            target = sorted_tasks[index]
            # Try to find the exact same object in self.tasks first
            for t in self.tasks:
                if t is target:
                    t.completed = True
                    break
                # Fallback: match by identity of important fields in case objects differ
                if (t.name == target.name and
                    t.priority == target.priority and
                    t.deadline == target.deadline and
                    t.duration == target.duration):
                    t.completed = True
                    break
            else:
                # Last fallback: mark the target itself
                target.completed = True
            self.save_tasks()

    def remove_completed(self):
        self.tasks = [t for t in self.tasks if not getattr(t, 'completed', False)]
        self.save_tasks()

    def remove_task(self, index):
        """Remove a single task referenced by the sorted view index."""
        sorted_tasks = self.sort_tasks()
        if 0 <= index < len(sorted_tasks):
            target = sorted_tasks[index]
            # Try identity match first
            for i, t in enumerate(self.tasks):
                if t is target:
                    del self.tasks[i]
                    self.save_tasks()
                    return True
            # Fallback: match by fields (name, priority, deadline, duration)
            for i, t in enumerate(self.tasks):
                if (t.name == target.name and
                    t.priority == target.priority and
                    t.deadline == target.deadline and
                    t.duration == target.duration):
                    del self.tasks[i]
                    self.save_tasks()
                    return True
        return False

    # Sort by deadline then priority
    def sort_tasks(self):
        return sorted(self.tasks, key=lambda t: (t.deadline, -t.priority))

    # Save tasks to JSON
    def save_tasks(self):
        data = []
        for t in self.tasks:
            data.append({
                "name": t.name,
                "priority": t.priority,
                "deadline": t.deadline.strftime("%d/%m/%Y %H:%M"),
                "duration": t.duration,
                "completed": getattr(t, 'completed', False)
            })
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    # Load tasks from JSON
    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                for item in data:
                    deadline = datetime.strptime(item["deadline"], "%d/%m/%Y %H:%M")
                    task = Task(item["name"], item["priority"], deadline, item["duration"])
                    task.completed = item.get("completed", False)
                    self.tasks.append(task)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

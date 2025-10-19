# task.py
from datetime import datetime

class Task:
    def __init__(self, name, priority, deadline, duration):
        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.duration = duration
        self.completed = False  # New field

    def display(self):
        formatted_deadline = self.deadline.strftime("%d/%m/%Y %H:%M")
        duration_minutes = int(self.duration * 60)
        status = "✅ Completed" if self.completed else "❌ Pending"
        print(f"Task: {self.name}, Priority: {self.priority}, Deadline: {formatted_deadline}, Duration: {duration_minutes} min(s), Status: {status}")

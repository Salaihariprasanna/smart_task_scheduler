# main.py
from scheduler import Scheduler
from datetime import datetime

def main():
    scheduler = Scheduler()

    while True:
        print("\n===== Smart Task Scheduler =====")
        print("1. Add Task")
        print("2. Show All Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("\nEnter Task Name: ").strip()

            try:
                priority = int(input("Enter Priority (1-5): ").strip())
                if priority < 1 or priority > 5:
                    print("❌ Priority must be between 1 and 5.")
                    continue
            except ValueError:
                print("❌ Invalid priority input! Must be a number (1–5).")
                continue

            # Deadline input
            deadline_input = input("Enter Deadline (dd/mm/yyyy hh:mm): ").strip()
            try:
                deadline = datetime.strptime(deadline_input, "%d/%m/%Y %H:%M")
            except ValueError:
                print("❌ Invalid date/time format! Use dd/mm/yyyy hh:mm (e.g., 20/10/2025 14:30).")
                continue

            # Duration input
            print("\nEnter Task Duration:")
            hours = input("  Hours: ").strip() or "0"
            minutes = input("  Minutes: ").strip() or "0"
            try:
                hours = float(hours)
                minutes = float(minutes)
                duration = hours + (minutes / 60)
            except ValueError:
                print("❌ Invalid duration input! Enter numbers only.")
                continue

            # Add task
            scheduler.add_task(name, priority, deadline, duration)
            print("✅ Task added successfully!")

        elif choice == '2':
            scheduler.show_tasks()

        elif choice == '3':
            print("\n👋 Exiting Smart Task Scheduler. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

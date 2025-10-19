# User Guide — Smart Task Scheduler

This user guide explains how to run and use the Smart Task Scheduler from the Web UI and the CLI, with examples and troubleshooting tips.

---

## Contents
1. Running the application  
2. Web UI — step-by-step  
3. CLI — step-by-step  
4. Example task entry  
5. Data format & manual edits  
6. Troubleshooting & tips

---

## 1. Running the application

Prerequisite: Python 3.8+ and Flask installed:
```sh
pip install flask
```

Start the Web UI:
```sh
python app.py
```
Open a browser at: http://127.0.0.1:5000

Start the CLI:
```sh
python main.py
```

---

## 2. Web UI — step-by-step

1. Open the main page served by `app.py`.
2. Fill the "Add New Task" form:
   - Name: free text (e.g., "Finish report")
   - Priority: integer 1 (highest) to 5 (lowest)
   - Deadline: exact format `dd/mm/YYYY HH:MM` (e.g., `25/10/2025 09:00`)
   - Duration: provide Hours (integer) and Minutes (integer) — the app converts to decimal hours
3. Click the submit button. The task will be listed on the page.
4. To mark a task as completed, click "Mark" next to the task.
5. To remove a single task, click "Remove".
6. To remove all completed tasks, click "Remove Completed".
7. Use the search or browser find to locate tasks on the page if the list grows long.

Notes:
- The UI displays tasks in the order returned by `Scheduler.sort_tasks`. To change ordering or apply smarter scheduling, update the scheduler code.

---

## 3. CLI — step-by-step

1. Run:
```sh
python main.py
```
2. Follow the menu prompts:
   - Option 1 — Add Task:
     - Enter task name
     - Enter priority (1–5)
     - Enter deadline in `dd/mm/YYYY HH:MM` format (e.g., `25/10/2025 09:00`)
     - Enter hours (integer) and minutes (integer) for duration
   - Option 2 — Show Tasks:
     - Displays tasks returned by `Scheduler.show_tasks()`; if output is minimal, edit `main.py` to format and print details using `Task.display()`
   - Option 3 — Exit

---

## 4. Example task entry

Add via Web UI or CLI with these values:
- Name: Finish report  
- Priority: 2  
- Deadline: 25/10/2025 09:00  
- Duration: 1 hour 30 minutes -> stored as 1.5

Resulting JSON entry in `tasks.json`:
```json
{
  "name": "Finish report",
  "priority": 2,
  "deadline": "25/10/2025 09:00",
  "duration": 1.5,
  "completed": false
}
```

---

## 5. Data format & manual edits

`tasks.json` stores an array of task objects. If you edit the file manually:
- Keep `deadline` strings formatted as `%d/%m/%Y %H:%M`
- Keep `duration` numeric as decimal hours
- Use boolean `completed` values (`true` / `false`)

If the JSON becomes invalid, the app may fail to load tasks — restore a backup or delete `tasks.json` to let the app recreate it.

---

## 6. Troubleshooting & tips

- Invalid deadline format error:
  - Ensure `dd/mm/YYYY HH:MM` exact format; leading zeros required where applicable.
- Permission denied saving `tasks.json`:
  - Run the app from a folder where you have write permission or change file permissions.
- Corrupt `tasks.json`:
  - Delete or restore the file; re-add tasks via UI or CLI.
- CLI shows no or poor output on "Show Tasks":
  - Modify `main.py` to iterate returned tasks and print formatted details (see example below).

Example CLI print improvement (edit `main.py`):
```py
# snippet to print tasks returned by scheduler.show_tasks()
tasks = scheduler.show_tasks()
if not tasks:
    print("No tasks found.")
else:
    for i, t in enumerate(tasks, 1):
        status = "✓" if t.completed else " "
        print(f"{i}. [{status}] {t.name} — Priority: {t.priority} — Deadline: {t.deadline} — Duration: {t.duration}h")
```

---

## Recommendations
- For interoperability, consider switching to ISO 8601 timestamps and store timezone-aware datetimes.
- If multiple processes may write `tasks.json`, add file locking to prevent corruption.
- Add unit tests for scheduler logic and persistence; mock or use temporary file paths for `tasks.json`.
- To implement advanced scheduling, write algorithms in `algorithm.py` and call them from `Scheduler.sort_tasks`.

---

End of User Guide.
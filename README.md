# Smart Task Scheduler

A small task scheduling application with a Flask web UI and a simple CLI. Add tasks (name, priority, deadline, duration), view tasks, mark complete, and remove tasks. Scheduling and ordering logic can be extended in `algorithm.py`.

This repository includes a bundled user manual: `USER_GUIDE.md`.

---

## Features
- Web UI (Flask) for adding, listing, completing and removing tasks
- Interactive CLI for basic operations
- JSON persistence (`tasks.json`)
- Pluggable scheduling algorithm placeholder (`algorithm.py`)

---

## Requirements
- Python 3.8+
- Install dependencies:
```sh
pip install flask
```

---

## Quick start

Run the web UI:
```sh
python app.py
```
Open: http://127.0.0.1:5000

Run the CLI:
```sh
python main.py
```

---

## Usage (summary / user guidance)
Web UI
- Add tasks via the "Add New Task" form:
  - Name (string)
  - Priority (1 = highest … 5 = lowest)
  - Deadline (format: `dd/mm/YYYY HH:MM`, e.g. `25/10/2025 09:00`)
  - Duration: Hours and Minutes (stored as decimal hours)
- Actions:
  - Mark — mark task completed
  - Remove — delete a single task
  - Remove Completed — delete all completed tasks
- Display order is determined by `Scheduler.sort_tasks` (customize for different scheduling behavior)

CLI
- Option 1 — Add Task: prompts for name, priority, deadline and duration
- Option 2 — Show Tasks: prints tasks returned by `Scheduler.show_tasks` (you may enhance `main.py` to format output)
- Option 3 — Exit

For a full step-by-step user manual and examples see `USER_GUIDE.md`.

---

## Data storage
- Tasks are persisted to `tasks.json` as an array of objects:
  - name: string
  - priority: integer
  - deadline: string (`%d/%m/%Y %H:%M`)
  - duration: float (hours, e.g., `1.5` = 1h30m)
  - completed: boolean

Do not change the deadline string format if you want the app to parse it correctly.

---

## Project files
- `algorithm.py` — scheduling algorithm placeholder / extension point  
- `app.py` — Flask web app and routes  
- `main.py` — CLI entry point  
- `scheduler.py` — Scheduler model, persistence, sorting, task management  
- `task.py` — Task model and helpers  
- `tasks.json` — persisted tasks file (created/updated by the app)  
- `templates/index.html` — web UI template  
- `USER_GUIDE.md` — detailed user manual (included in this repo)

---

## Extending the scheduler
- Implement algorithms in `algorithm.py` (e.g., `compute_order(tasks: list[Task]) -> list[Task]`)  
- Integrate by calling / replacing `Scheduler.sort_tasks` in `scheduler.py`  
- If you add fields to `Task` (in `task.py`), update serialization in `Scheduler.save_tasks` / `Scheduler.load_tasks`

---

## Developer notes & recommendations
- Deadline parsing/formatting uses `%d/%m/%Y %H:%M`. Consider switching to ISO 8601 if interoperability is required.
- Add file locking (e.g., using portalocker) if multiple processes may write `tasks.json`.
- Add unit tests under `tests/` and mock file I/O or use temporary files for Scheduler tests.
- Improve CLI output by iterating the list from `Scheduler.show_tasks()` and calling `Task.display()` or formatting entries manually.

---

## Troubleshooting
- Invalid deadline format: ensure `dd/mm/YYYY HH:MM` exactly (e.g., `25/10/2025 09:00`).
- Permission errors writing `tasks.json`: ensure write permission in project directory.
- Corrupt `tasks.json`: restore or delete the file; the app will recreate it on next save.

---

## License
Add a LICENSE file with your preferred license (e.g., MIT, Apache-2.0).


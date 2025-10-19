# app.py
from flask import Flask, render_template, request, redirect
from scheduler import Scheduler
from datetime import datetime

app = Flask(__name__)
scheduler = Scheduler()

@app.route('/')
def index():
    tasks = scheduler.show_tasks()
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    name = request.form.get('name')
    priority = int(request.form.get('priority'))
    deadline_str = request.form.get('deadline')
    hours = float(request.form.get('hours', 0))
    minutes = float(request.form.get('minutes', 0))
    duration = hours + minutes / 60
    deadline = datetime.strptime(deadline_str, "%d/%m/%Y %H:%M")
    scheduler.add_task(name, priority, deadline, duration)
    return redirect('/')

@app.route('/complete/<int:index>')
def complete_task(index):
    scheduler.mark_completed(index)
    return redirect('/')

@app.route('/remove/<int:index>')
def remove_task(index):
    # Remove a single task referenced by the sorted view index
    scheduler.remove_task(index)
    return redirect('/')

@app.route('/remove_completed')
def remove_completed():
    scheduler.remove_completed()
    return redirect('/')

if __name__ == "__main__":
    import os, webbrowser, threading, time

    def _open_browser():
        time.sleep(1)               # give the server a moment to start
        webbrowser.open_new("http://127.0.0.1:5000/")

    # When debug=True, the reloader runs the module twice; only open browser in the reloader child
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true" or not app.debug:
        threading.Thread(target=_open_browser).start()

    app.run(debug=True)

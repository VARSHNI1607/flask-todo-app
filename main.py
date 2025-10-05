from flask import Flask, render_template, request, redirect, jsonify
from datetime import datetime
import json
from replit import db

app = Flask(__name__)

# Load tasks from DB
if "tasks" in db:
    tasks = json.loads(db["tasks"])
else:
    tasks = []

def save_tasks():
    db["tasks"] = json.dumps(tasks)

def next_id():
    if tasks:
        return max(task["id"] for task in tasks) + 1
    else:
        return 1

def sort_tasks(tasks_list):
    def parse_date(task):
        return datetime.strptime(task["deadline"], "%Y-%m-%d") if task["deadline"] else datetime.max
    return sorted(tasks_list, key=parse_date)

@app.route("/")
def index():
    today = datetime.today().date().isoformat()
    sorted_tasks = sort_tasks(tasks)
    daily_tasks = [t for t in sorted_tasks if t["deadline"] == today and not t["completed"]]
    return render_template("index.html", tasks=sorted_tasks, daily_tasks=daily_tasks, today=today)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    category = request.form.get("category")
    deadline = request.form.get("deadline")
    priority = request.form.get("priority")
    if title:
        tasks.append({
            "id": next_id(),
            "title": title,
            "category": category,
            "deadline": deadline,
            "priority": priority,
            "completed": False
        })
        save_tasks()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t["id"] != id]
    save_tasks()
    return redirect("/")

@app.route("/complete/<int:id>")
def complete_task(id):
    for t in tasks:
        if t["id"] == id:
            t["completed"] = not t["completed"]
            break
    save_tasks()
    return redirect("/")

@app.route("/get_task/<int:id>")
def get_task(id):
    for t in tasks:
        if t["id"] == id:
            return jsonify(t)
    return jsonify({})

@app.route("/edit/<int:id>", methods=["POST"])
def edit_task(id):
    for t in tasks:
        if t["id"] == id:
            t["title"] = request.form.get("title")
            t["category"] = request.form.get("category")
            t["deadline"] = request.form.get("deadline")
            t["priority"] = request.form.get("priority")
            break
    save_tasks()
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)

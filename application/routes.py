from application import app, db
from application.models import Tasks
from application.forms import TaskForm
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    all_tasks = Tasks.query.all()
    return render_template('index.html', title="Home", all_tasks=all_tasks)
    
@app.route('/create/task', methods=['GET', 'POST'])
def create_task():
    form = TaskForm()
    
    if request.method == 'POST':
        new_task = Tasks(description=form.description.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("create_task.html", title="Add a new task", form=form)

@app.route('/read/alltasks')
def read_tasks():
    all_tasks = Tasks.query.all()
    tasks_dict = {"tasks":[]}
    for task in all_tasks:
        tasks_dict["tasks"].append(
            {
                "description": task.description,
                "completed": task.completed
            }
        )
    return tasks_dict

@app.route('/update/task/<int:id>', methods =['GET','POST'])
def update_task(id):
    form = TaskForm()

    task = Tasks.query.get(id)

    if request.method == 'POST':
        task.description = form.description.data
        db.session.commit()
        return redirect(url_for('home'))
    
    db.session.commit()
    return render_template('update_task.html', task=task, form=form)

@app.route('/delete/task/<int:id>')
def delete(id):
    id_to_delete = Tasks.query.get(id)
    db.session.delete(id_to_delete)
    db.session.commit()
    return f"Deleted {id}"

@app.route('/complete/task/<int:id>')
def completed(id):
    task = Tasks.query.get(id)
    task.completed = True
    db.session.commit()
    return f"Task {id} marked as completed"

@app.route('/incomplete/task/<id>')
def incomplete(id):
    task = Tasks.query.get(id)
    task.completed = False
    db.session.commit()
    return f"Task {id} marked as incomplete"
from flask import Flask,render_template,url_for,flash
from werkzeug.utils import redirect

from models import db,Task
from forms import TaskForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "wahab747575757"

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_BASE = os.path.join(BASE_DIR, "instance","todo.db")

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATA_BASE}'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/',methods=['GET','POST'])
def home():
    form = TaskForm()

    if form.validate_on_submit():
        new_task = Task(title=form.title.data,)
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully!", "success")
        return redirect(url_for('home'))

    tasks = Task.query.all()
    completed_tasks = Task.query.filter_by(completed=True).count()
    total_tasks = Task.query.count()
    return render_template('index.html',form=form,tasks=tasks,completed_tasks=completed_tasks,total_tasks=total_tasks)

@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    task = db.get_or_404(Task,task_id)
    task.completed = not task.completed
    db.session.commit()
    flash("Task updated.", "info")


    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>',methods=['GET','POST'])
def delete(task_id):
    task = db.get_or_404(Task,task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted.", "danger")
    return redirect(url_for('home'))





if __name__ == '__main__':
    app.run(debug=True)
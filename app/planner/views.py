from flask import Blueprint, request, render_template, redirect, url_for
from app.helpers import get_date_from_date_string
from ..tasks.models import Task
from ..tasks.forms import TaskForm
from ..database import db


planner = Blueprint('planner', __name__, url_prefix='/planner')


@planner.route('/date')
@planner.route('/date/<regex("[0-9]{4}-[0-9]{2}-[0-9]{2}"):date_string>')
def show_tasks_by_date(date_string=None):
    if not date_string:
        date_string = request.args['date']
    try:
        date = get_date_from_date_string(date_string)
    except ValueError:
        return render_template("layout/custom_error_page.html", problem="Incorrect date",
                               message="We can't show tasks from this day because the date requested is incorrect.")
    tasks = Task.query.filter(Task.date == date).all()
    return render_template("planner/date_index.html", tasks=tasks, date_string=date_string)


@planner.route('/date/<regex("[0-9]{4}-[0-9]{2}-[0-9]{2}"):date_string>/add', methods=['GET', 'POST'])
def add_task_by_date(date_string):
    form = TaskForm(request.form)
    if request.method == "POST" and form.validate():
        task = Task(name=form.name.data,
                    date=form.date.data,
                    priority=form.priority.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('planner.show_tasks_by_date', date_string=date_string))
    else:
        form.date.data = get_date_from_date_string(date_string)
        return render_template('tasks/form.html',
                               form=form,
                               submit_string="Add")
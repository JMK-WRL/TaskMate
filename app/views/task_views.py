# app/views/task_views.py
from flask import Blueprint, render_template, request, jsonify
from app.models import Task

task_bp = Blueprint('task', __name__)

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify(tasks=[task.serialize() for task in tasks])

@task_bp.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if task:
        return jsonify(task.serialize())
    else:
        return jsonify({'message': 'Task not found'}), 404

@task_bp.route('/task', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(title=data['title'], description=data['description'], status=data['status'])
    # Add additional fields as needed
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully'}), 201

# Add more routes and views as needed

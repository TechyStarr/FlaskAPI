from apiflask import APIFlask, abort
from db import session, Task
from flask import jsonify
from schemas import TaskOutputSchema, TaskCreateSchema, TaskUpdateSchema


app = APIFlask(__name__)


@app.get("/")
def index():
	return {"message":'Hello World'}
	

'''
	get /task get_all_task
	post /task create_tast
	get /task/<task_id> get_task_by_id
	put /task/<task_id> update_task
	delete /task/<task_id> delete_task
'''

@app.get('/tasks')
def get_all_tasks():
    posts = session.query(Task).all()
    schema = TaskOutputSchema()
    result = schema.dump(posts, many=True)
    return jsonify(result)
	
@app.post('/tasks')
@app.input(TaskCreateSchema)
@app.output(TaskOutputSchema)
def create_task(data):
	content = data.get("content")
	new_task = Task(content = content)
	session.add(new_task)
	session.commit()

	return new_task, 201 

@app.get('/tasks/<int:task_id>')
def get_task_by_id(task_id):
	task = session.query(Task).filter_by(id=task_id).first()
	if task is not None:
		return task, 200

	abort(404, "You don't have a task")


@app.put('/tasks/<int:task_id>')
@app.input(TaskUpdateSchema)
@app.output(TaskOutputSchema)
def update_task(task_id, data):
	content = data.get("content")
	is_completed = data.get('is_completed')
	update_task = session.query(Task).filter_by(id=task_id).first()
	update_task.content = content
	update_task.is_completed = is_completed
	session.commit()
	return update_task, 201


@app.delete('/tasks/<int:task_id>')
def delete_task(task_id):
	deleted_task = session.query(Task).filter_by(id=task_id).first()
	session.delete(deleted_task)


	abort(201, "You have deleted a task")

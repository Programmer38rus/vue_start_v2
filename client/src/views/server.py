import bottle
from truckpad.bottle.cors import CorsPlugin, enable_cors
from db_operations import form_list, add_task_to_db, delete_task, change_task

app = bottle.Bottle()

@enable_cors
@app.route("/api/tasks/")
def index():
    db_list = form_list()
    db_on_dict = [child.to_dict() for child in db_list]

    return {"tasks": db_on_dict}

@enable_cors
@app.route("/api/add-task/", method="POST")
def add_task():
    json = bottle.request.json
    add_task_to_db(json)

    return "ОК - добавлена новая задача"


@enable_cors
@app.route("/api/tasks/<uid>", method=["GET", "PUT", "DELETE"])
def show_or_modify_task(uid):
    if bottle.request.method == "GET":
        print("we is in the func!")
        return tasks_db[uid].to_dict()
    elif bottle.request.method == "PUT":
        task = bottle.request.json
        print(task)
        change_task(uid, task)

        return f'Modified task {uid}'

    elif bottle.request.method == "DELETE":
        delete_task(uid)

        return f"Deleted task {uid}"

@bottle.route("/api/complete/<uid:int>")
def api_complete(uid):
    tasks_db[uid].is_completed = True
    return "OK"

app.install(CorsPlugin(origins=['http://localhost:5000']))

if __name__ == "__main__":
    bottle.run(app, host="localhost", port=5000)

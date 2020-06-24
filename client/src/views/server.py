import bottle
from truckpad.bottle.cors import CorsPlugin, enable_cors

app = bottle.Bottle()

class Todoitem:
    def __init__(self, descriprion, unique_id):
        self.description = descriprion
        self.is_completed = False
        self.uid = unique_id

    def __str__(self):
        return self.description.lower()

    def to_dict(self):
        return {
            "description": self.description,
            "is_completed": self.is_completed,
            "uid": self.uid
        }


task_list = ["написать код",
             "покормить морскую свинку",
             "постирать кроссовки",
             "поесть еды"
             ]

tasks_db = {
    uid: Todoitem(desc, uid)
    for uid, desc in enumerate(iterable=task_list, start=1)
}

@enable_cors
@app.route("/api/tasks")
def index():
    # bottle.response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    tasks = [task.to_dict() for task in tasks_db.values()]
    for i in tasks_db.values():
        print(i)
    return {"tasks": tasks}

@enable_cors
@app.route("/api/add-task/", method="POST")
def add_task():
    desc = bottle.request.json['description']
    is_completed = bottle.request.json['is_completed']

    if len(desc) > 0:
        new_uid = max(tasks_db.keys()) + 1
        t = Todoitem(desc, new_uid)
        t.is_completed = is_completed
        tasks_db[new_uid] = t
    return "OK"


@bottle.route("/api/delete/<uid:int>")
def api_delete(uid):
    tasks_db.pop(uid)
    return "OK"


@bottle.route("/api/complete/<uid:int>")
def api_complete(uid):
    tasks_db[uid].is_completed = True
    return "OK"

app.install(CorsPlugin(origins=['http://localhost:5000']))

###
if __name__ == "__main__":
    bottle.run(app, host="localhost", port=5000)

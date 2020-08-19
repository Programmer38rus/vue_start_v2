import bottle
from truckpad.bottle.cors import CorsPlugin, enable_cors
from db_operations import form_list, add_task_to_db, delete_task, change_task

app = bottle.Bottle()

# class Todoitem:
#     def __init__(self, descriprion, unique_id):
#         self.description = descriprion
#         self.is_completed = False
#         self.uid = unique_id
#
#     def __str__(self):
#         return self.description.lower()
#
#     def to_dict(self):
#         return {
#             "description": self.description,
#             "is_completed": self.is_completed,
#             "uid": self.uid
#         }
#
#
# task_list = ["написать код",
#              "покормить морскую свинку",
#              "постирать кроссовки",
#              "поесть еды"
#              ]
#
# tasks_db = {
#     uid: Todoitem(desc, uid)
#     for uid, desc in enumerate(iterable=task_list, start=1)
# }
# print(tasks_db)

@enable_cors
@app.route("/api/tasks/")
def index():
    # tasks = [task.to_dict() for task in tasks_db.values()]
    # for i in tasks_db.values():
    #     print(i)
    # return {"tasks": tasks}

    db_list = form_list()
    db_on_dict = [child.to_dict() for child in db_list]

    return {"tasks": db_on_dict}

@enable_cors
@app.route("/api/add-task/", method="POST")
def add_task():
    # desc = bottle.request.json['description']
    # is_completed = bottle.request.json['is_completed']
    #
    # if len(desc) > 0:
    #     new_uid = max(tasks_db.keys()) + 1
    #     t = Todoitem(desc, new_uid)
    #     t.is_completed = is_completed
    #     tasks_db[new_uid] = t
    # return "OK"
    json = bottle.request.json
    add_task_to_db(json)

    return "ОК - добавлена новая задача"



@enable_cors
@app.route("/api/tasks/<uid:int>", method=["GET", "PUT", "DELETE"])
def show_or_modify_task(uid):
    if bottle.request.method == "GET":
        print("we is in the func!")
        return tasks_db[uid].to_dict()
    elif bottle.request.method == "PUT":
        # if "description" in bottle.request.json:
        #     tasks_db[uid].description = bottle.request.json["description"]
        # if "is_completed" in bottle.request.json:
        #     tasks_db[uid].is_completed = bottle.request.json["is_completed"]
        task = bottle.request.json
        print(task)
        change_task(uid, task)

        return f'Modified task {uid}'
    elif bottle.request.method == "DELETE":
        # tasks_db.pop(uid)
        delete_task(uid)

        return f"Deleted task {uid}"

# @bottle.route("/api/delete/<uid:int>")
# def api_delete(uid):
#     tasks_db.pop(uid)
#     return "OK"
#     delete_task(uid)



@bottle.route("/api/complete/<uid:int>")
def api_complete(uid):
    tasks_db[uid].is_completed = True
    return "OK"

app.install(CorsPlugin(origins=['http://localhost:5000']))

###
if __name__ == "__main__":
    bottle.run(app, host="localhost", port=5000)

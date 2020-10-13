from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

task1 = [{"id": 1, "name": "frontend Development"},
         {"id": 2, "name": "backend Development"},
         {"id": 3, "name": "Database Development"}]

task2 = [{"id": 1, "name": "facebook"},
         {"id": 2, "name": "watsapp"},
         {"id": 3, "name": "instagram"}]

task3 = [{"id": 1, "name": "message"},
         {"id": 2, "name": "email"},
         {"id": 3, "name": "SMS"}]

developers = [{"id": 1, "name": "developer1", "task": task1},
              {"id": 2, "name": "developer2", "task": task2},
              {"id": 3, "name": "developer3", "task": task3}]


class Developers(Resource):
    def get(self):
        items = []
        for developer in developers:
            items.append(developer["name"])
        return items


class Tasks(Resource):
    def get(self):
        items = []
        for developer in developers:
            for task in developer["task"]:
                items.append(task["name"])
            return items


class DevelopersWithId(Resource):
    def get(self, id):
        for developer in developers:
            if id == developer["id"]:
                return jsonify({"name": developer["name"]})
            else:
                return "Please enter id from 1 to 3"


class DevelopersWithIdTasks(Resource):
    def get(self, id):
        items = []
        for developer in developers:
            if id == developer["id"]:
                for tasks in developer["task"]:
                    items.append(tasks["name"])
                return items
            else:
                return "Please enter id from 1 to 3"


class DevelopersWithIdTasksWithId(Resource):
    def get(self, id, tid):
        for developer in developers:
            if id == developer["id"]:
                for tasks in developer["task"]:
                    if tasks["id"]==tid:
                        return tasks["name"]
                    else:
                        return "Please enter task id from 1 to 3"
            else:
                return "Please enter developer id from 1 to 3"


api.add_resource(Developers, '/developers')
api.add_resource(Tasks, '/tasks')
api.add_resource(DevelopersWithId, '/developers/<int:id>')
api.add_resource(DevelopersWithIdTasks, '/developers/<int:id>/tasks')
api.add_resource(DevelopersWithIdTasksWithId,
                 '/developers/<int:id>/tasks/<int:tid>')


if __name__ == '__main__':
    app.run(debug=True)

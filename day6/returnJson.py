from flask import Flask,jsonify

app=Flask(__name__)

items=[{"name":"john","id":4},{"name":"smith","id":5}]

@app.route('/')
def personDetails():
    return jsonify({"item":items})



if __name__ == '__main__':
    app.run(debug=True)
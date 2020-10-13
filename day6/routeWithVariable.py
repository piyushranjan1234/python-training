from flask import Flask

app=Flask(__name__)

@app.route('/')
def helloWorld():
    return "hello world"

@app.route('/customers/<id>') #without defining the type
def customers(id):
    return f"customer having id :{id}"


@app.route('/items/<string:item>') # defining the type
def items(item):
    return f"the item is :{item}"


if __name__ == '__main__':
    app.run(debug=True)
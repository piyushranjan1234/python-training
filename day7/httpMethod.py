from flask import Flask, request

app = Flask(__name__)


def do_the_login():
    return "Login confirm"


def show_the_login_form():
    return "login with User data "


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


@app.route('/customers/<int:id>', methods=['PUT'])
def customers(id):
    if request.method == 'PUT':
        return f"customer having id :{id}"


@app.route('/items/<int:id>',methods=['DELETE'])
def items(id):
    if request.method == 'DELETE':
        return f"the item of id :{id} is deleted"


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello my flask"


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return "submit success"
    elif request.method =="GET":
        return "submit list"

@app.route("/user/<username>")
def get_user(username):
    return f"Hi, {username}"

@app.route("/square/<int:number>")
def square(number):
    result = number ** 2
    return "{} squared is {}".format(number, result)

@app.route("/welcome/<name>")
def username(name):
    return f"welcome! {name}"

@app.route("/multiply/<int:a>/<int:b>")
def multiply(a,b):
    result = a * b
    return f"{a} * {b} = {a*b}"

@app.route("/api/data", methods = ["GET", "POST"])
def api_data():
    if request.method == "GET":
        print(request)
        return {"status": "ok"}
    else:
        data = request.get_json()
        print(data)
        print(type(data))
        # print(request.data.get('username'))
        return jsonify({'status': 'posted', "username": data.get('username')}), 201
    


    

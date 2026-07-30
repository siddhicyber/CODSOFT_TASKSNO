from flask import Flask, request

app = Flask(__name__)

username = "admin"
password = "12345"

@app.route('/login')
def login():
    user = request.args.get('username')
    pwd = request.args.get('password')

    if user == username and pwd == password:
        return "Login Successful"

    return "Invalid Login"

app.run(debug=True)
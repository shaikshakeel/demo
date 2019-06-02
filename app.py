from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/gopal")
def gopal():
	return jsonify(
		{
			'msg' : 'success',
			'text' : 'hello world'
		}
	)

@app.route("/api/v1/users/gangs/all")
def all():
	return jsonify(
		{
			'a' : 'b',
			'c' : 'd'
		}
	)

app.run(debug=True)
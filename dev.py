from flask import Flask

app = Flask(_name_)

@app.route("/info")
def info():
	return "hello myself sambhav jain"

@app.route("/phone")
def myphone():
	return "9772019175"

app.run(host="0.0.0.0")

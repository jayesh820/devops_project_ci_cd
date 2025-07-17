from flask import Flask

app = Flask(_name_)

@app.route("/info")
def info():
	return "hello my name is jayesh"

@app.route("/phone")
def myphone():
	return "218472019175"

app.run(host="0.0.0.0")

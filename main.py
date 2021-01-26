from flask import Flask

app = Flask(_name_)

@app.route("/")
def hello():
    return "<h1> Not much going on here</h1>"

app.run(host='0.0.0.0', port=80)
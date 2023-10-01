from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_tim():
    return "<p>Hello Tim!</p>"
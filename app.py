from flask import Flask

app = Flask(__name__)

@app.route("/")
def Owescool():
    test = "<p>Owes is the coolest team ever!</p>"
    return test 
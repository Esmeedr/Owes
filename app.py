from flask import Flask

app = Flask(__name__)

@app.route("/")
def Owescool():
    return "<p>Owes is the coolest team ever!</p>"
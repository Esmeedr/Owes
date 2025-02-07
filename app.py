from flask import Flask

app = Flask(__name__)

@app.route("/")
def Owescool():
    return "<p>werkt het nu wel dan?</p>"
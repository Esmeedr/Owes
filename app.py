from flask import Flask

app = Flask(__name__)

@app.route("/")
def Owescool():
    test = "<p>Dit is een test leuk hea!</p>"
    return test 

from flask import Flask
from flask import render_template,url_for,request,redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

if __name__=="__main__":
    app.debug=True
    app.run(port=8888)

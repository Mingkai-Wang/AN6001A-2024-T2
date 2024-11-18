1
#don't forget type 1 after comment then syncomment

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run(port=1111)
1#
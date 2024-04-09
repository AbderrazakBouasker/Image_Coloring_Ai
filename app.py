from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.get("/results")
def results():
    # Load the JSON file containing images and image URLs
    with open("data.json") as file:
        data = json.load(file)
        print("test")
    return render_template("results.html", images=data)

@app.post("/colorize")
def colorize():
    return 

if __name__ == "__main__":
    app.run()
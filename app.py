from flask import Flask, flash, redirect, render_template, request
from dl_copy import colorize_image
from werkzeug.utils import secure_filename
import os

import json
from PIL import Image  
import PIL  

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

# @app.post("/colorize")
# def colorize():
#     image = request.files.get("image")
#     # Save the image
#     image.save("image.jpg")
#     # Load the model
#     colorize_image("image")
#     # Return the colorized image
#     return render_template("index.html", colorized_image_url="result_image.jpg")

# def allowed_file(filename):
#     """Check if the filename has an allowed file extension."""
#     ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
#     return '.' in filename and \
#         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    

@app.post("/colorize")
def colorize():
    if "image" not in request.files:
        flash("No file part")
        return redirect(request.url)

    image = request.files["image"]

    if image.filename == "":
        flash("No selected file")
        return redirect(request.url)

    if image:
        #filename = secure_filename(image.filename)
        # filepath = os.path.join(app.config["static"], filename)
        image.save("image.jpg")

        # Call function to colorize the image
        colorized_filepath = colorize_image("image.jpg")

        # Return the colorized image URL to the template
        return render_template("index.html", colorized_image_url=colorized_filepath)
        #return render_template("index.html", colorized_image_url="image_result.jpg")

    flash("Invalid file type")
    return redirect(request.url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

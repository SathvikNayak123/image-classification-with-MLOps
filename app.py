from flask import Flask, request, render_template
import numpy as np
from PIL import Image
import io
import os
from src.cnnClassifier.pipeline.predict_pipeline import Prediction

# Initialize the Flask app
app = Flask(__name__)
prediction_model = Prediction()

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    predicted_class = None
    image_url = None

    if request.method == "POST":
        # Get the uploaded file
        file = request.files["file"]
        if file:
            # Save the image to the static/uploads directory
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)

            # Read the image file
            image = Image.open(file)
            image = np.array(image)

            # Make a prediction
            predicted_class = prediction_model.predict_class(image)

            # Set the image URL for displaying
            image_url = f"/{file_path}"

    return render_template("index.html", predicted_class=predicted_class, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

# Load the trained CIFAR-10 CNN model
MODEL_PATH = "cifar10_cnn_model.keras"
model = load_model(MODEL_PATH)

# CIFAR-10 class names
CLASS_NAMES = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck"
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "CIFAR-10 CNN Flask API is running!",
        "endpoint": "/predict"
    })


@app.route("/predict", methods=["POST"])
def predict():

    # Check whether an image was uploaded
    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded. Use the key 'image'."
        }), 400

    image_file = request.files["image"]

    if image_file.filename == "":
        return jsonify({
            "error": "No image selected."
        }), 400

    try:
        # Open image
        image = Image.open(image_file).convert("RGB")

        # Resize image to CIFAR-10 input size
        image = image.resize((32, 32))

        # Convert image to NumPy array
        image_array = np.array(image)

        # Normalize pixel values
        image_array = image_array / 255.0

        # Add batch dimension
        image_array = np.expand_dims(image_array, axis=0)

        # Make prediction
        prediction = model.predict(image_array, verbose=0)

        # Get predicted class
        predicted_index = np.argmax(prediction[0])
        predicted_class = CLASS_NAMES[predicted_index]

        # Get confidence
        confidence = float(prediction[0][predicted_index]) * 100

        return jsonify({
            "prediction": predicted_class,
            "confidence": round(confidence, 2),
            "class_index": int(predicted_index)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

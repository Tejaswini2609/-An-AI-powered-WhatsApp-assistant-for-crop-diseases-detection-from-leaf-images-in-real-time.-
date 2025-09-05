import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os, json

# Paths
MODEL_PATH = os.path.join("model", "model.h5")
CLASS_INDICES_PATH = os.path.join("model", "class_indices.json")

# Load model
model = tf.keras.models.load_model(MODEL_PATH)

# Load classes
with open(CLASS_INDICES_PATH, "r") as f:
    class_indices = json.load(f)
idx_to_class = {v: k for k, v in class_indices.items()}

def predict_disease(img_path):
    """Preprocess image and predict plant disease"""
    try:
        # Preprocess image (match training size)
        img = image.load_img(img_path, target_size=(128, 128))  
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Predict
        prediction = model.predict(img_array)
        class_idx = np.argmax(prediction, axis=1)[0]
        confidence = np.max(prediction)

        return f"{idx_to_class[class_idx]} (confidence: {confidence:.2f})"
    except Exception as e:
        return f"Prediction failed: {str(e)}"

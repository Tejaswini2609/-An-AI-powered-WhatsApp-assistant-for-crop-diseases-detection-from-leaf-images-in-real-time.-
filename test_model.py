import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json

# --------------------------
# Step 1: Paths
# --------------------------
MODEL_PATH = r"C:\Users\Tejaswini D\OneDrive\Desktop\Crop-assistant\model\model.h5"
CLASS_INDICES_PATH = r"C:\Users\Tejaswini D\OneDrive\Desktop\Crop-assistant\model\class_indices.json"
TEST_IMAGE_PATH = r"C:\Users\Tejaswini D\OneDrive\Desktop\Crop-assistant\data\image (955).JPG"

print("🚀 Starting test script...")

# --------------------------
# Step 2: Load Model + Classes
# --------------------------
try:
    print("🔄 Loading model...")
    model = load_model(MODEL_PATH)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    exit()

try:
    print("🔄 Loading class indices...")
    with open(CLASS_INDICES_PATH, "r") as f:
        class_indices = json.load(f)
    idx_to_class = {v: k for k, v in class_indices.items()}
    print("✅ Class indices loaded!")
except Exception as e:
    print(f"❌ Error loading class indices: {e}")
    exit()

# --------------------------
# Step 3: Load and Preprocess Image
# --------------------------
if not os.path.exists(TEST_IMAGE_PATH):
    print(f"❌ Test image not found at {TEST_IMAGE_PATH}")
    exit()

print("🔄 Loading test image...")
img = image.load_img(TEST_IMAGE_PATH, target_size=(128, 128))  # match training size
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0
print("✅ Test image loaded and preprocessed!")

# --------------------------
# Step 4: Prediction
# --------------------------
print("🔮 Running prediction...")
predictions = model.predict(img_array)
predicted_class = np.argmax(predictions, axis=1)[0]
confidence = np.max(predictions)

print(f"🌱 Predicted Disease: {idx_to_class[predicted_class]} (Confidence: {confidence:.2f})")

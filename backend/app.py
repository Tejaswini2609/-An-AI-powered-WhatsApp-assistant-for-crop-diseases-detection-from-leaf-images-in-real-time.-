from flask import Flask, request
from utils.helper import predict_disease
import os
import requests
from twilio.twiml.messaging_response import MessagingResponse
from PIL import Image
import io
import uuid

app = Flask(__name__)

# Temp folder for downloaded images
UPLOAD_FOLDER = "temp"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --------------------------
# Helper function: download Twilio image
# --------------------------
def download_twilio_image(media_url, folder="temp"):
    os.makedirs(folder, exist_ok=True)
    
    # Read Twilio credentials from environment variables
    TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
    
    if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN:
        raise ValueError("Twilio credentials not set in environment variables")
    
    # Download media with authentication
    r = requests.get(media_url, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN))
    
    # Validate content type
    if "image" not in r.headers.get("Content-Type", ""):
        raise ValueError(f"URL does not point to an image. Content-Type: {r.headers.get('Content-Type')}")
    
    # Open and save image
    img = Image.open(io.BytesIO(r.content))
    img_path = os.path.join(folder, f"{uuid.uuid4()}.jpg")
    img.save(img_path)
    
    return img_path

# --------------------------
# Test Route
# --------------------------
@app.route("/ping", methods=["GET"])
def ping():
    return {"message": "pong 🏓"}, 200

# --------------------------
# WhatsApp Webhook
# --------------------------
@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    resp = MessagingResponse()

    # Number of media files sent
    num_media = int(request.form.get("NumMedia", 0))
    if num_media == 0:
        resp.message("Please send an image of your crop to get a prediction.")
        return str(resp)

    # Get the first media URL
    media_url = request.form.get("MediaUrl0")
    if not media_url:
        resp.message("Could not retrieve the image. Try again.")
        return str(resp)

    # Download and save the image
    try:
        img_path = download_twilio_image(media_url)
    except Exception as e:
        resp.message(f"Prediction failed: {str(e)}")
        return str(resp)

    # Run prediction
    try:
        prediction = predict_disease(img_path)
    except Exception as e:
        os.remove(img_path)
        resp.message(f"Prediction failed: {str(e)}")
        return str(resp)

    # Delete temporary image
    os.remove(img_path)

    # Send prediction back via WhatsApp
    resp.message(f"Prediction: {prediction}")
    return str(resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

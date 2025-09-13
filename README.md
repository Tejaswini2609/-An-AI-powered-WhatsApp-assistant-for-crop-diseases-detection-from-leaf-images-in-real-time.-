#🌱 "WhatsApp-Based LeafSense AI"
#An AI-powered WhatsApp assistant that helps farmers detect crop diseases from leaf images in real time. Farmers simply send a photo via WhatsApp, and the system responds with the predicted disease and confidence score.
✨ Features
📷 Detect crop diseases from leaf images
💬 Seamless integration with WhatsApp
🤖 Deep learning–based prediction (TensorFlow/Keras)
📊 Provides disease name + confidence level
🌍 Easy to use for farmers, no extra apps required

🛠️ Tech Stack
Backend: Flask (Python)
AI Model: TensorFlow / Keras
Messaging: WhatsApp API (Twilio or alternatives)
Image Processing: Pillow, NumPy

🚀 How It Works
Farmer sends a crop leaf image through WhatsApp.
Flask server receives the image via WhatsApp API.
The AI model processes the image and predicts the disease.
Result (disease + confidence score) is sent back to the farmer on WhatsApp.

📂 Project Structure
├── backend/              # Flask app files
│   ├── app.py            # Main Flask server
│   ├── utils/            # Helper functions
│   └── models/           # Trained ML/DL models
├── temp/                 # Temporary storage for images
├── requirements.txt      # Dependencies
└── README.md             # Project documentation

⚡ Installation & Setup
# Clone the repository
git clone https://github.com/your-username/crop-disease-whatsapp-assistant.git
# Navigate to project folder
cd crop-disease-whatsapp-assistant
# Install dependencies
pip install -r requirements.txt
# Run the Flask server
python app.py

📱 WhatsApp Integration
Use Twilio WhatsApp Sandbox (or another API) to connect the Flask webhook.
Configure your webhook URL in the messaging platform dashboard.
Send a crop image via WhatsApp → get instant prediction.

🎯 Applications
Early detection of crop diseases
Helps farmers prevent yield loss
Makes AI accessible through WhatsApp

📸 Demo
<img width="1375" height="1080" alt="imlementation" src="https://github.com/user-attachments/assets/7c926ca8-385e-4147-b4bc-4f945d2bf4c3" />

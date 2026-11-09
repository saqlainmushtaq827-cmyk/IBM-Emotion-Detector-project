IBM Emotion Detector Project
Final Project

An AI-powered Emotion Detection application built using Python, Flask, and a locally running Hugging Face emotion classification model.

Features
Detects anger, disgust, fear, joy, and sadness.
Identifies the dominant emotion.
Provides emotion confidence scores.
Flask web interface.
Local AI model inference.
Technologies
Python
Flask
Hugging Face Transformers
PyTorch
Run the application

Install dependencies:

bash
pip install flask transformers torch


Start the application:

bash
python server.py


Open your browser:

text
http://127.0.0.1:5000/

Project structure
text
IBM-Emotion-Detector-project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── server.py
└── README.md


Final Project
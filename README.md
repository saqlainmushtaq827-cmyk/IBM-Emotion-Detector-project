
# Emotion Detector

## Project Overview

The Emotion Detector is an AI-powered web application that
analyzes text and identifies the emotions expressed in it
using the IBM Watson Natural Language Processing library.

The application detects five different emotions:

1. Anger
2. Disgust
3. Fear
4. Joy
5. Sadness

It also identifies the dominant emotion in the submitted text.

## Technologies Used

- Python
- IBM Watson NLP
- Flask
- Requests
- HTML
- CSS
- JavaScript
- Unittest
- Pylint

## Project Structure

```text
Emotion-Detector/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── templates/
│   └── index.html
│
├── test_emotion_detection.py
├── server.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/Emotion-Detector.git
```

Navigate into the project:

```bash
cd Emotion-Detector
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Flask application:

```bash
python server.py
```

Open your browser and visit:

http://127.0.0.1:5000

## Run Unit Tests

Execute:

```bash
python -m unittest -v test_emotion_detection.py
```

## Static Code Analysis

Execute:

```bash
pylint server.py
```

## Features

- Detects five human emotions.
- Identifies the dominant emotion.
- Provides a simple web interface.
- Handles empty input.
- Handles invalid service responses.
- Includes automated unit tests.

## Author

Emotion Detector Final Project.

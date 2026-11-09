
"""
Flask server for the Emotion Detector application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Display the home page."""

    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """Analyze the submitted text and return emotion results."""

    text_to_analyze = request.args.get("textToAnalyze", "")

    # Handle blank input.
    if not text_to_analyze.strip():
        return "Please enter some text!", 400

    # Call the emotion detection function.
    result = emotion_detector(text_to_analyze)

    # Handle invalid requests or service errors.
    if result is None:
        return "Invalid text or emotion service unavailable.", 400

    response = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )

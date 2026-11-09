
"""
Local Emotion Detection using Hugging Face.
"""

from transformers import pipeline

MODEL_NAME = "j-hartmann/emotion-english-distilroberta-base"

classifier = None


def emotion_detector(text_to_analyze):
    """Detect five emotions using a local AI model."""

    global classifier

    if not isinstance(text_to_analyze, str):
        return None

    if not text_to_analyze.strip():
        return None

    try:
        if classifier is None:
            print("Loading emotion detection model...")

            classifier = pipeline(
                "text-classification",
                model=MODEL_NAME,
                top_k=None,
                device=-1
            )

            print("Model loaded successfully!")

        predictions = classifier(text_to_analyze.strip())

        if predictions and isinstance(predictions[0], list):
            predictions = predictions[0]

        scores = {
            "anger": 0.0,
            "disgust": 0.0,
            "fear": 0.0,
            "joy": 0.0,
            "sadness": 0.0
        }

        for prediction in predictions:
            label = prediction["label"].lower()

            if label in scores:
                scores[label] = float(prediction["score"])

        scores["dominant_emotion"] = max(
            scores,
            key=scores.get
        )

        return scores

    except Exception as error:
        print("Emotion Detection Error:", error)
        return None

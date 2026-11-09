
"""
Unit tests for the Emotion Detection application.
"""

import unittest
from unittest.mock import patch, Mock

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test the emotion detection functionality."""

    def create_mock_response(self, emotions):
        """Create a mock Watson API response."""

        mock_response = Mock()

        mock_response.status_code = 200

        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": emotions
                }
            ]
        }

        return mock_response

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, mock_post):
        """Test dominant joy emotion."""

        mock_post.return_value = self.create_mock_response({
            "anger": 0.01,
            "disgust": 0.02,
            "fear": 0.03,
            "joy": 0.90,
            "sadness": 0.04
        })

        result = emotion_detector("I am happy!")

        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, mock_post):
        """Test dominant anger emotion."""

        mock_post.return_value = self.create_mock_response({
            "anger": 0.90,
            "disgust": 0.02,
            "fear": 0.03,
            "joy": 0.01,
            "sadness": 0.04
        })

        result = emotion_detector("I am angry!")

        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, mock_post):
        """Test dominant sadness emotion."""

        mock_post.return_value = self.create_mock_response({
            "anger": 0.01,
            "disgust": 0.02,
            "fear": 0.03,
            "joy": 0.04,
            "sadness": 0.90
        })

        result = emotion_detector("I feel sad.")

        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear(self, mock_post):
        """Test dominant fear emotion."""

        mock_post.return_value = self.create_mock_response({
            "anger": 0.01,
            "disgust": 0.02,
            "fear": 0.90,
            "joy": 0.04,
            "sadness": 0.03
        })

        result = emotion_detector("I am afraid.")

        self.assertEqual(result["dominant_emotion"], "fear")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust(self, mock_post):
        """Test dominant disgust emotion."""

        mock_post.return_value = self.create_mock_response({
            "anger": 0.01,
            "disgust": 0.90,
            "fear": 0.02,
            "joy": 0.03,
            "sadness": 0.04
        })

        result = emotion_detector("That is disgusting.")

        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_empty_input(self):
        """Test empty input."""

        result = emotion_detector("")

        self.assertIsNone(result)

    def test_whitespace_input(self):
        """Test whitespace input."""

        result = emotion_detector("   ")

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()

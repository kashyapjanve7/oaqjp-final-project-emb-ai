"""Unit tests for the emotion detector."""

import json
import unittest
from unittest.mock import Mock, patch
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test cases for emotion_detector function."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector(self, post):
        """Test all five required statements with Watson-compatible responses."""
        cases = (
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        )
        for statement, expected_emotion in cases:
            scores = {
                emotion: 0.9 if emotion == expected_emotion else 0.025
                for emotion in ("anger", "disgust", "fear", "joy", "sadness")
            }
            post.return_value = Mock(
                status_code=200,
                text=json.dumps({"emotionPredictions": [{"emotion": scores}]}),
            )
            with self.subTest(statement=statement):
                result = emotion_detector(statement)
                self.assertEqual(result["dominant_emotion"], expected_emotion)


if __name__ == "__main__":
    unittest.main()

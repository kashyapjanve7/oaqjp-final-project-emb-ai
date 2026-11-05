# Final Project

A Flask web app that analyzes customer feedback with the Watson NLP emotion prediction service and reports anger, disgust, fear, joy, sadness, and the dominant emotion.

## Setup

```bash
python -m pip install requests flask
python server.py
```

The app uses the Skills Network Theia lab emotion service by default. Set `EMOTION_API_URL` to a compatible endpoint when running elsewhere. The lab endpoint may only be reachable from the Skills Network environment.

Open `http://127.0.0.1:5000/` and submit feedback. Blank input is rejected with HTTP 400. Service or response failures produce an explicit unavailable result.

## Tests and static analysis

```bash
python -m unittest -v
python -m pylint server.py emotion_detection.py EmotionDetection
```

The GitHub URL and screenshots requested by the course must be produced from an account and browser session you control; they cannot be fabricated by this local project.

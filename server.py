"""
Flask application to detect emotions from a given text using a machine learning model.

This module provides an endpoint to analyze the emotions in the text
passed as a query parameter and returns the detected emotions.
"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def sent_analyzer():
    """Analyze the emotions in the provided text and return the results.

    Returns:
        str: A string summarizing the detected emotions and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, "
        f"and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

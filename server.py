"""
This module contains the Flask web application for emotion detection.

It includes two routes:
1. The `/emotionDetector` route, which takes a text input, analyzes it for emotions, 
   and returns the detected emotions and the dominant emotion.
2. The `/` route, which renders the main index page of the application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Detect the emotion from the provided text.

    This function retrieves the text to analyze from the request arguments,
    passes it to the emotion_detector function, and returns the response in a formatted way.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result is None:
        return "Invalid text! Please try again."

    return (f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
            f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}.")

@app.route("/")
def render_index_page():
    """
    Render the main index page of the application.

    This function initiates the rendering of the main application page over the Flask channel.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

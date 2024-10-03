from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=['GET'])
def sent_analyzer():
    '''
    Detect emotion
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Check if the text_to_analyze is provided
    if not text_to_analyze:
        return "Invalid input! Try again."

    # Pass the text to the emotion_detector function and store the response
    result = emotion_detector(text_to_analyze)

    # Check if the result is None or if there's an error in the response
    if result is None:
        return "Invalid input! Try again."

    # Return a formatted string with the emotion scores
    return (f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
            f"'joy': {result['joy']}, and "
            f"'sadness': {result['sadness']}. The dominant emotion "
            f"is {result['dominant_emotion']}.")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

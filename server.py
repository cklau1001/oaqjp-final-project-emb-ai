"""
The Flask app to provide emotion detection of incoming text.

"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    The emotion detection endpoint to perform analysis on input text
    :return
      the emotion score as a text statement
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    result = f"""
    For the given statement, the system response is 'anger': {response['anger']},
    'digust': {response['disgust']}, 'fear': {response['fear']}, 
    'joy': {response['joy']} and 'sadness': {response['sadness']}. 
    The dominant emotion is 
    <strong style='font-weight: 500'>{response['dominant_emotion']}</strong>.
    """

    return result

@app.route("/")
def render_index_page():
    """
    To render the home page
    :return
       the html content of home page
    """
    return render_template('/index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
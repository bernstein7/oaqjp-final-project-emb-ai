from flask import Flask, request, render_template
import json

from EmotionDetection import emotion_detector

app = Flask(__name__) 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detection():
    text = request.args["textToAnalyze"]
    results = emotion_detector(text)

    response = "For the given statement, the system response is "    

    for index, (key, value) in enumerate(results.items()):
        if key == "dominant_emotion":
            continue
        if (index < len(results.items()) - 2):
            response += f"'{key}': {value}, "
        else:
            response += f"and '{key}': {value}.\n"

    dominant_emotion = results["dominant_emotion"]
    response += f"The dominant emotion is {dominant_emotion}."

    return response, 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

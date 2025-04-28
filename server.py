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
    if not text:
        return "Invalid text! Please try again!.", 200

    results = emotion_detector(text)
    dominant_emotion = results["dominant_emotion"]
    
    if not dominant_emotion:
        return "Invalid text! Please try again!.", 200

    response = "For the given statement, the system response is "    

    for index, (key, value) in enumerate(results.items()):
        if key == "dominant_emotion":
            continue
        if (index < len(results.items()) - 2):
            response += f"'{key}': {value}, "
        else:
            response += f"and '{key}': {value}.\n"

    
    response += f"The dominant emotion is {dominant_emotion}."

    return response, 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

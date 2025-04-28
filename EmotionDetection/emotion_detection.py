import requests

EMOTION_DETECTOR_URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"


def emotion_detector(text_to_analyze) -> dict:
    body = { "raw_document": { "text": text_to_analyze } }
    headers = __build_headers()
    response = requests.post(EMOTION_DETECTOR_URL, headers=headers, json=body)

    if response.status_code == 400:
        return __default_dict()

    result = response.json()

    emotions = result["emotionPredictions"][0]["emotion"]
    emotions = {k: v for k, v in sorted(emotions.items(), key=lambda item: item[1], reverse=True)}
    dominant_emotion = list(emotions.keys())[0]
    return emotions | {"dominant_emotion": dominant_emotion}

    
def __build_headers() -> dict:
    return {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

def __default_dict() -> dict:
    return {
        'joy': None,
        'sadness': None,
        'anger': None,
        'fear': None,
        'disgust': None,
        'dominant_emotion': None
    }

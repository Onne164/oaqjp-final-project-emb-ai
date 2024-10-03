import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze or text_to_analyze.strip() == "":
        # If text is blank, return None values for each emotion
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 400:
        # Return None for invalid inputs from server
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parse the response JSON
    result = json.loads(response.text)

    # Extract emotion scores
    emotions = result['emotionPredictions'][0]['emotion']

    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Return formatted result
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

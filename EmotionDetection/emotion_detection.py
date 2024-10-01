import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Send POST request to Watson API
    response = requests.post(url, headers=headers, json=input_json)

    # Ensure response status is OK
    if response.status_code == 200:
        # Parse the response into a dictionary
        response_data = json.loads(response.text)
        
        # Extract the emotion scores
        emotions = response_data['emotionPredictions'][0]['emotion']
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        
        # Determine the dominant emotion (emotion with the highest score)
        emotion_scores = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return the formatted output
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    else:
        return "No text found in the response"

# Example usage
if __name__ == "__main__":
    text = "I love this new technology."
    result = emotion_detector(text)
    print(result)

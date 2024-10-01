import requests

# Define the emotion detector function
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    # The input JSON payload
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Make the POST request to Watson's Emotion Predict API
    response = requests.post(url, json=input_json, headers=headers)
    
    # If the request is successful, return the response
    if response.status_code == 200:
        return response.json()
    else:
        return "Error: Unable to get emotion analysis"

import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=input_json, headers=header)
    formated_response = json.loads(response.text)

    # Extracting emotion values
    if response.status_code == 200:
        anger = formated_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formated_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formated_response['emotionPredictions'][0]['emotion']['fear']
        joy = formated_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formated_response['emotionPredictions'][0]['emotion']['sadness']

        # Creating a dictionary to find the dominant emotion
        dominant_emo = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness}
        dominant_emotion = max(dominant_emo, key=dominant_emo.get)
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None
    else:
        # Handle other response statuses if necessary
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}

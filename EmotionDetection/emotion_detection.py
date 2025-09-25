"""
A simple module to perform emotion analysis using IBM Watsion AI

"""
import json
import requests

def emotion_detector(text_to_analyse: str) -> dict:
    """
    Perform emotion analysis on incoming text
    :arg
        text_to_analyse (str): incoming text

    :return
        the emotion metrics in a dictionary
    """
    ibm_url = "https://sn-watson-emotion.labs.skills.network/v1"
    watson_uri = "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    url = f"{ibm_url}/{watson_uri}"

    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=300)
    formatted_response = json.loads(response.text)

    emotion_response = formatted_response['emotionPredictions'][0]['emotion']

    emotion_response = {
        'anger': float(emotion_response["anger"]),
        'disgust': float(emotion_response["disgust"]),
        'fear': float(emotion_response["fear"]),
        'joy': float(emotion_response["joy"]),
        'sadness': float(emotion_response["sadness"]),            
    }
    sorted_emotion_list = sorted(emotion_response.items(), key=lambda item: item[1], reverse=True)
    dominant_emotion = sorted_emotion_list[0][0]
    emotion_response['dominant_emotion'] = dominant_emotion

    return emotion_response

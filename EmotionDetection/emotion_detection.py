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

    emotion_response = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None
    }

    response = requests.post(url, json = myobj, headers=header, timeout=300)
    if response.status_code == 400:
        emotion_response['dominant_emotion'] = None
        return emotion_response

    formatted_response = json.loads(response.text)
    emotion_block = formatted_response['emotionPredictions'][0]['emotion']
    emotion_response['anger'] = float(emotion_block["anger"])
    emotion_response['disgust'] = float(emotion_block["disgust"])
    emotion_response['fear'] = float(emotion_block["fear"])
    emotion_response['joy'] = float(emotion_block["joy"])
    emotion_response['sadness'] = float(emotion_block["sadness"])

    sorted_emotion_list = sorted(emotion_response.items(), key=lambda item: item[1], reverse=True)
    dominant_emotion = sorted_emotion_list[0][0]
    emotion_response['dominant_emotion'] = dominant_emotion

    return emotion_response

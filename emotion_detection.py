"""
A simple module to perform emotion analysis using IBM Watsion AI

"""
import requests

def emotion_detector(text_to_analyse: str):
    """
    Perform emotion analysis on incoming text
    :arg
        text_to_analyse (str): incoming text

    :return
        the result
    """
    ibm_url = "https://sn-watson-emotion.labs.skills.network/v1"
    watson_uri = "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    url = f"{ibm_url}/{watson_uri}"

    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=300)

    return response.text

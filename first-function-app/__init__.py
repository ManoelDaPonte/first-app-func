import logging
import os
import azure.functions as func
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import SpeechRecognizer, SpeechConfig, AudioConfig


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    speech_key = os.environ["SpeechSubscriptionKey"]
    service_region = 'westeurope'
    speech_config = SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_recognition_language = "fr-FR" # set the language to French
    audio_config = AudioConfig(filename=req.files['audio'].filename)

    recognizer = SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    result = recognizer.recognize_once()

    return func.HttpResponse(result.text)
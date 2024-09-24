import speech_recognition as sr
from ui.gui import *





def detect_wake_word(keyword, recognizer, microphone):
    print("Listening for wake word...")
    while True:
        with microphone as source:
            audio = recognizer.listen(source, phrase_time_limit=5)

        try:
            transcript = recognizer.recognize_google(audio, language=('hi, en')).lower()
            update_prompt(transcript)
            print(transcript)
            if keyword in transcript:
                print("Wake word detected!")
                return transcript

        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Could not request results; check your network connection.")
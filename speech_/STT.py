import speech_recognition as sr


recognizer = sr.Recognizer()
microphone = sr.Microphone()

def STT():

##-------STT----------##

    print("Listening for command...")
    with microphone as source:
        recognizer.energy_threshold = 1000
        #recognizer.adjust_for_ambient_noise(source, duration=5)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
    try:
        prompt = recognizer.recognize_google(audio, language='hi, en')
        print(f"You said: {prompt}")
        return prompt
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        prompt = ""
        return prompt
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        prompt = ""
        return prompt
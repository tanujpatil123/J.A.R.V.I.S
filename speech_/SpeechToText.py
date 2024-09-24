import speech_recognition as sr


recognizer = sr.Recognizer()
microphone = sr.Microphone()

def STT():

##-------STT----------##

    print("Listening for command...")
    with microphone as source:
        audio = recognizer.listen(source)
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
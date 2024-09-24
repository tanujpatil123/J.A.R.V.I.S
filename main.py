import speech_recognition as sr
from action.wake import *
import playsound
from speech_.TTS import *
from speech_.STT import *
from brain import *
from process_handler.action import *
from ui.gui import *
from Images.gen_image import *
from action.findmyip import *
from action.whatsapp import *
from Images.capture_image import *
from action.checkweather import *
from Images.vision import *



exit_event = threading.Event()


recognizer = sr.Recognizer()
microphone = sr.Microphone()
keyword = "jarvis"


def start_gui():
    gui_appear()


        
if __name__ == '__main__':
    gui_thread = threading.Thread(target=start_gui)
    gui_thread.start()
    awake=True

    #detect_wake_word(keyword, recognizer, microphone)
    print("Yes Sir, what we are doing today.")    
    playsound.playsound("wake.mp3")

    while True:
        #intent = brain("Write a code for a simple python game").text
        query = detect_wake_word(keyword, recognizer, microphone)
        if query == None:
            continue
        else:
            query = query.lower()
            intent = brain(query).text



        print(query)
        print(intent)

        if intent == None:
            TTS(intent)

        elif 'ACTION_AWAKEN' in intent:
            awake=True            
            TTS("How can I help you Sir?")            
            continue

        elif 'ACTION_SLEEP' in intent:
            awake=False
            TTS("Hibernating now")
            gui.sleep()
            continue

        elif not awake:
            print("Currently hibernating...Zzzz...nothing to do.")
            continue

        elif 'ACTION_EXIT' in intent:
            TTS('Have a good day Sir')
            gui.close_window(exit_event)
            exit(1)

        elif 'ACTION_OPEN_NOTEPAD' in intent:
            open_notepad()
            TTS_en("Done Sir.")

        elif 'ACTION_OPEN_WORD' in intent:
            open_word()
            TTS_en("Done Sir.")

        elif 'ACTION_OPEN_EXCEL' in intent:
            open_excel()
            TTS_en("Done Sir.")

        elif 'ACTION_OPEN_POWERPOINT' in intent:
            open_ppt()
            TTS_en("Done Sir.")

        elif 'ACTION_OPEN_COMMAND_PROMPT' in intent:
            open_cmd()
            TTS_en("Done Sir.")
		
        elif 'ACTION_OPEN_CALCULATOR' in intent:
            open_calculator()
            TTS_en("Done Sir.")
                    
        elif "ACTION_TAKE_SCREENSHOT" in intent:
            take_screenshot()
            TTS_en("Done Sir.")
        
        elif "ACTION_START_SCREEN_RECORDING" in intent:
            start_screen_record()
            TTS_en("Done Sir.")
        
        elif "ACTION_STOP_SCREEN_RECORDING" in intent:
            stop_screen_record()
            TTS_en("Done Sir.")

        elif "ACTION_OPEN_CAMERA" in intent:
            open_camera()
            TTS_en("Done Sir.")

        elif intent.startswith("action_search"):
            print("Searching for.........")
            exec(intent)
            TTS_en("Done Sir.")

            
        elif intent.startswith("open_browser"):
            open_browser()
            TTS_en("Done Sir.")

        elif intent.startswith("ACTION_OPEN_STICKYNOTES"):
            open_stickynotes()
            TTS_en("Done Sir.")

        elif intent.startswith("generate_image"):
            TTS("Yes Sir, Please wait some time.")
            exec(intent)
            TTS_en("Done Sir.")

        elif intent.startswith("pyautogui.write"):
            exec(intent)
            TTS_en("Done Sir.")

        elif intent.startswith("pyautogui.hotkey"):
            exec(intent)
            TTS_en("Done Sir.")

        elif intent.startswith("pyautogui.press"):
            exec(intent)
            TTS_en("Done Sir.")

        elif intent.startswith("ip()"):
            exec(intent)
            TTS_en("Done Sir.")

        elif intent.startswith("whatsapp("):
            exec(intent)
            TTS_en("Done Sir.")

        elif intent.startswith("youtube_search"):
            exec(intent)
            TTS_en("Done Sir.")

        elif intent.startswith("open_youtube"):
            exec(intent)
            TTS_en("Done Sir.")

        elif intent.startswith("cap_img()"):
            exec(intent)
            TTS_en("Done Sir.")

        elif intent.startswith("vision()"):
            exec(intent)
            TTS_en("Done Sir.")

        elif intent.startswith("weather()"):
            exec(intent)
            TTS_en("Done Sir.")

        else:
            TTS(intent)




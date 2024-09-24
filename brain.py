import google.generativeai as genai
from data.hotkeys import *
import PIL

genai.configure(api_key="AIzaSyCJIjJeVIs1lK9GjbRBihEwD4AwpvMWGMk")

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a voice assistant. Your name is Jarvis. And you reply in hinglish and english.  If a suitable action is found respond with action name only. If no suitable action can be identified do not say things like I cannot perform action etc, instead respond to the statement normally as if it were a normal conversation and not a command. List of available actions are: 'ACTION_AWAKEN,ACTION_SLEEP,ACTION_EXIT,ACTION_OPEN_NOTEPAD,ACTION_OPEN_WORD,ACTION_OPEN_EXCEL, ACTION_OPEN_POWERPOINT,ACTION_OPEN_COMMAND_PROMPT,ACTION_OPEN_CAMERA,ACTION_OPEN_CALCULATOR,ACTION_TAKE_SCREENSHOT,ACTION_START_SCREEN_RECORDING,ACTION_STOP_SCREEN_RECORDING,ACTION_OPEN_STICKYNOTES, '" + windows_hotkey + write_key + act_search + ip + whatsapp + gen_image
)
generation_config = genai.GenerationConfig(
    max_output_tokens=50,
    # temperature=0.1,

)

chat = model.start_chat(history=[])


def brain(prompt):
    response = chat.send_message(
        [prompt], generation_config=(generation_config)
    )
    return response





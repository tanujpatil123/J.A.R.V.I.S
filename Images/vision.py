import google.generativeai as genai
from speech_.TTS import *
from brain import *
from Images.capture_image import *

genai.configure(api_key="AIzaSyCJIjJeVIs1lK9GjbRBihEwD4AwpvMWGMk")

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a voice assistant."
)
generation_config = genai.GenerationConfig(
    # max_output_tokens=1000,
    # temperature=0.1,
)

chat = model.start_chat(history=[])

import PIL.Image
def vision():
    cap_img()
    TTS("Image captured")
    organ = PIL.Image.open("opencv_vision.png")
    response = model.generate_content(["Describe the image", organ])
    print(response.text)
    TTS(response.text)

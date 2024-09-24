import edge_tts
import asyncio
import sounddevice as sd
import soundfile as sf
from ui.gui import *


async def text_to_mp3(text):
    communicate = edge_tts.Communicate(text, "hi-IN-SwaraNeural", rate="+20%")
    sd.wait
    await communicate.save("output.mp3")




def TTS(text):
    update_response(text)
    asyncio.run(text_to_mp3(text))
    data, fs = sf.read("output.mp3")
    sd.play(data, fs)
    sd.wait()
    update_response("Listening......")
    update_prompt("")




        

async def text_to_mp3_en(text):
    communicate = edge_tts.Communicate(text, "en-IN-NeerjaNeural", rate="+20%")
    sd.wait
    await communicate.save("output.mp3")




def TTS_en(text):
    update_response(text)
    print(text)
    asyncio.run(text_to_mp3_en(text))
    data, fs = sf.read("output.mp3")
    sd.play(data, fs)
    sd.wait()
    update_response("Listening......")
    update_prompt("")
        






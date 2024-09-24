import requests
from PIL import Image
from io import BytesIO
import time
from speech_.TTS import *
from brain import *
from Images.capture_image import *

image_path = 'opencv_vision.png'


def generate_image(text):
    TTS("Yes Sir, Please wait sometime.")
    url = 'https://api.airforce/v1/imagine2'
    params = {'prompt': text}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.save('generated_image.png')
        print('Image saved as generated_image.png')
        im = Image.open("generated_image.png")
        im.show()
        TTS("Done Sir, anyting else")
        time.sleep(3)       
    else:
        print(f'Failed to retrieve image. Status code: {response.status_code}')




def what_vision():
    cap_img()
    TTS("Image captured")
    organ = PIL.Image.open("opencv_vision.png")
    response = model.generate_content(["Describe the image", organ])
    print(response.text)
    TTS(response.text)



    
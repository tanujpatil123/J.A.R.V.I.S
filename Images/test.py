from brain import *

image_path = 'opencv_vision.png'

def what_vision():
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    response = chat.send_message(
        model='gemini-1.5-flash',
        contents=[{'type': 'image', 'data': image_data}]
    )
    print(response['text'])


what_vision()
import cv2



def cap_img():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('opencv_vision.png', image)
    del(camera)

cap_img()
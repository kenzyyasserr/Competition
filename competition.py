import cv2
import numpy as np

cam = cv2.VideoCapture(0)
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

class_list = []

def preprocess(img, size=(128, 128)):
    img_resized = cv2.resize(img, size)
    img_resized = img_resized.astype("float32") / 255.0
    img_resized = np.expand_dims(img_resized, axis=0)
    return img_resized

def process_image(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = (40, 40, 40)
    upper_green = (70, 255, 255)
    mask = cv2.inRange(hsv, lower_green, upper_green)
    letter_img = cv2.bitwise_and(frame, frame, mask=mask)

    letter = None
    if letter is not None:
        class_list.append(letter)

    sign = None
    return sign if sign else None

def detect_sign(frame):
    sign = None
    if sign in ["arrow_left", "arrow_right"]:
        return sign
    return None

while True:
    ret, frame = cam.read()
    if not ret:
        break

    out.write(frame)
    cv2.imshow('Camera', frame)

    sign = process_image(frame)
    if sign:
        print("Detected sign:", sign)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
out.release()
cv2.destroyAllWindows()

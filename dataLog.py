# To be run during manual control of robot
import cv2
import tensorflow as tf

objectCoor = []

# file path to the .h5 model
modelPath = ""

model = tf.keras.model.load_model(modelPath)

cam = cv2.VideoCapture(0)
while True:
    # bool if image exists
    ret, img = cam.read()
    if ret == True:
        cv2.imwrite("img.jpg",img)
        model.evaluate() #input image
        objectCoor.append() # append with the coordinates of two corners from model.evaluate()
        # obtain data from vex
        # write data to csv? file for training the main model
        # train initial model for reinforcement autonomous driving in separate program

# release video stream and close windows
cam.release()
cv2.destroyALLWindows()


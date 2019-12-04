import cv2

cam = cv2.VideoCapture(0)
while True:
    # bool if image exists
    ret, img = cam.read()
    if ret == True:
        cv2.imshow("webcam",img)
        if cv2.waitKey(1) == ord("q"):
            break
    else:
        print("No image to display")

# release video stream and close windows
cam.release()
cv2.destroyALLWindows()


import cv2

cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 
frames_per_second = cap.get(cv2.CAP_PROP_FPS)



cv2.namedWindow("My 1st Video Streamer")
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("My 1st Video Streamer", frame)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
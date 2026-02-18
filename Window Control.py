

import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype=np.uint8)

drawing = False
ix, iy = -1, -1

def draw_rect(event, x, y, flags, param):
    global drawing, ix, iy
    color = (2, 10, 100)

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.rectangle(img, (ix, iy), (x, y),color , -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.namedWindow("My Sketch")
cv2.setMouseCallback("My Sketch", draw_rect)

while True:
    cv2.imshow("My Sketch", img)
    key = cv2.waitKey(1) & 0xFF

    # ESC or 'k' to exit
    if key == 27 or key == ord('k'):
        break

    # Close if window is manually closed
    if cv2.getWindowProperty("My Sketch", cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()



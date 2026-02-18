import cv2
import numpy as np

# Create a black image
img = np.zeros((500, 500, 3), dtype=np.uint8)

# Mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Draw a filled circle at (x, y)
        cv2.circle(img, (x, y), 20, (0, 255, 0), -1)

# Create window
cv2.namedWindow("Draw Circle")
cv2.setMouseCallback("Draw Circle", draw_circle)

while True:
    cv2.imshow("Draw Circle", img)
    key = cv2.waitKey(1) & 0xFF

    # Press 'q' to quit
    if key == ord('q'):
        break

cv2.destroyAllWindows()

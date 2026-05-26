import cv2
import numpy as np
from collections import deque

def capture_background(cap, frames=60):
    """Background capture jab object nahi ho frame me"""
    buffer = deque(maxlen=30)
    for i in range(frames):
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv2.flip(frame, 1)
        buffer.append(frame)
        cv2.putText(frame, "Capturing background... Stay out of frame!",
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.imshow("Background", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyWindow("Background")
    return np.median(np.array(buffer), axis=0).astype(np.uint8)

def get_mask_for_dark_blue(frame):
    """Dark blue color ke liye HSV mask"""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Dark blue HSV range
    lower_blue = np.array([100, 100, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Morphological operations for clean mask
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=1)

    return mask

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Camera access failed.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    print("Capturing background... Please stay out of frame.")
    background = capture_background(cap)

    print("Background captured. Cloak mode activated!")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)

        # Mask for dark blue cloak
        mask = get_mask_for_dark_blue(frame)
        mask_inv = cv2.bitwise_not(mask)

        # Background where cloak is present
        cloak_area = cv2.bitwise_and(background, background, mask=mask)

        # Current frame where cloak is NOT present
        visible_area = cv2.bitwise_and(frame, frame, mask=mask_inv)

        # Final output
        final_output = cv2.addWeighted(cloak_area, 1, visible_area, 1, 0)

        cv2.putText(final_output, "Dark Blue Cloak Mode - Press 'q' to quit",
                    (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Invisibility Cloak", final_output)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
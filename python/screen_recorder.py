import cv2
import numpy as np
import pyautogui
import time

def screen_recorder(output_file='output.avi', fps=20.0, duration=10):
    # Get the screen size
    screen_size = pyautogui.size()

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, fps, screen_size)

    print("Recording...")

    start_time = time.time()
    while True:
        # Capture the screen
        img = pyautogui.screenshot()
        
        # Convert the image to a numpy array
        frame = np.array(img)
        
        # Convert the color from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Write the frame
        out.write(frame)

        # Check if the duration has been reached
        if time.time() - start_time > duration:
            break

    # Release the video writer
    out.release()
    print("Recording finished.")

if __name__ == "__main__":
    screen_recorder(output_file='output.avi', fps=20.0, duration=10)

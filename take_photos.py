import cv2
import datetime

# Define desired resolution
width = 640
height = 480

# Initialize video capture object with default camera (0)
cap = cv2.VideoCapture(0)

# Set camera resolution (might not be supported by all cameras)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is captured successfully
    if not ret:
        print("Error: Could not capture frame")
        break

    # Display the resulting frame
    cv2.imshow('Take Photo (press space to capture)', frame)

    # Wait for user input (q to quit, space to capture)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord(' '):  # Capture photo on space key press
        # Get current timestamp
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # Save the frame with timestamp
        filename = f"photo_{now}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Photo saved as: {filename}")

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()

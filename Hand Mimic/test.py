import cv2

# Initialize the camera capture
cap = cv2.VideoCapture(0)  # 0 is typically the default camera (you can change it to a different camera index if needed)

# Define the coordinates of the ROI

x, y, width, height = 300, 000, 700, 700  # Example values, adjust these as needed

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was successfully captured
    if not ret:
        break

    # Get the height of the frame
    frame_height = frame.shape[0]

    # Adjust the Y-coordinate to invert the Y-axis
    # y = frame_height - y - height
    # print(y)
    # Crop the frame to the ROI
    frame = frame[y:y+height, x:x+width]

    # Display the cropped ROI
    cv2.imshow('ROI', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

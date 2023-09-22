import cv2
from objectLogic import analyze_image
from time import sleep
# Initialize the camera
cap = cv2.VideoCapture(0)
x, y, width, height = 300, 000, 700, 700  # Example values, adjust these as needed

# while True:
    # Capture a frame from the camera
ret, frame = cap.read()
frame_height = frame.shape[0]

# Adjust the Y-coordinate to invert the Y-axis
# y = frame_height - y - height
# print(y)
# Crop the frame to the ROI
frame = frame[y:y+height, x:x+width]
# Display the camera preview

# cv2.imshow('Camera Preview', frame)
if ret:
     # Save the screenshot as "screenshot.png"
    cv2.imwrite('sample.jpg', frame)
    print("Screenshot saved as 'screenshot.png'")
    analyze_image()
# Wait for a key press 
    # analyze_image()
# # If 'q' is pressed, quit the program
#     key = cv2.waitKey(1)
#     if key & 0xFF == ord('q'):
#         break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

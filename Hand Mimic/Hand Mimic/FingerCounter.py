import cv2
import mediapipe as mp
x, y, width, height = 300, 000, 700, 700 
cap = cv2.VideoCapture(0)
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands()
mpDraw = mp.solutions.drawing_utils
finger_Coord = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumb_Coord = (4,2)

while True:
    success, image = cap.read()
    image_height = image.shape[0]
    image = image[y:y+height, x:x+width]
    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(RGB_image)
    multiLandMarks = results.multi_hand_landmarks
    if multiLandMarks:
        handList = []
        for handLms in multiLandMarks:
            mpDraw.draw_landmarks(image, handLms, mp_Hands.HAND_CONNECTIONS)
            for idx, lm in enumerate(handLms.landmark):
              h, w, c = image.shape
              cx, cy = int(lm.x * w), int(lm.y * h)
              handList.append((cx, cy))
        for point in handList:
            cv2.circle(image, point, 10, (255, 255, 0), cv2.FILLED)
        upCount = 0
        for coordinate in finger_Coord:
            if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                upCount += 1
        
        if handList[thumb_Coord[0]][0] > handList[thumb_Coord[1]][0]:
            upCount+= 1
        # # pointer finger
        # if handList[finger_Coord[0][0]][1]< handList[finger_Coord[0][1]][1]:
        #     pointer_finger=1
        # else:
        #     pointer_finger=0
        # #middle finger     
        # if handList[finger_Coord[1][0]][1]< handList[finger_Coord[1][1]][1]:
        #     middle_finger=1
        # else:
        #     middle_finger=0
        # #ring finger
        # if handList[finger_Coord[2][0]][1]< handList[finger_Coord[2][1]][1]:
        #     ring_finger=1
        # else:
        #     ring_finger=0
        # #pinky finger
        # if handList[finger_Coord[3][0]][1]< handList[finger_Coord[3][1]][1]:
        #     pinky_finger=1
        # else:
        #     pinky_finger=0
        # #thumb_finger 
        # if handList[thumb_Coord[0]][0] > handList[thumb_Coord[1]][0]:
        #     thumb_finger= 1
        # else:
        #     thumb_finger=0
        # msg = [thumb_finger,pointer_finger,middle_finger,ring_finger,pinky_finger]
        cv2.putText(image, str(upCount), (150,150), cv2.FONT_HERSHEY_PLAIN, 4, (0,255,0), 6)

    cv2.imshow("Finger detection :", image)
    cv2.waitKey(1)
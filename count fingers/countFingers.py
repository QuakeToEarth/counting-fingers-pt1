import cv2
import mediapipe as mp
cam = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_join = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.5)
tipID = [8,12,16,20]
def drawLandmakrs(img,hand_landmarks):
    if hand_landmarks:
        for landmark in hand_landmarks:
            mp_join.draw_landmarks(img,landmark,mp_hands.HAND_CONNECTIONS)




while True:
    ret,img = cam.read()
    img = cv2.flip(img,1)
    results = hands.process(img)
    hand_landmarks = results.multi_hand_landmarks
    drawLandmakrs(img, hand_landmarks)
    cv2.imshow('count the fingers pls', img)
    if cv2.waitKey(1) == 32:
        break
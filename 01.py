import cv2
import mediapipe as mp
import pyautogui
capture = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
ring_y = 0
while True:
    success, frame = capture.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(color_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 55, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                if id == 12:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 55, 255))
                    ring_x = screen_width/frame_width*x
                    ring_y = screen_height/frame_height*y
                    print('outside', abs(index_y - ring_y))
                    if abs(index_y - ring_y) < 30:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    elif abs(index_y + ring_y) > 50:
                        pyautogui.moveTo(index_x*1.3, index_y*1.3)
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
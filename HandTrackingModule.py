import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, 1, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=False):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        # print(self.results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNo=0):
        lmList = []
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

            indexX = 0
            indexY = 0
            indexMid = 0
            handBottomX = 0
            handBottomY = 0
            pinkyX = 0
            pinkyY = 0
            fistWarning = "Fist!"
            for lms in lmList:
                if lms[0] == 7:
                    indexX, indexY = lms[1], lms[2]
                    # cv2.circle(handsFrame, (lms[1], lms[2]), 15, (255, 0, 255), cv2.FILLED)
                elif lms[0] == 5:
                    indexMid = lms[2]
                # elif lms[0] == 11:
                # middleY = lms[2]
                # cv2.circle(handsFrame, (lms[1], lms[2]), 15, (255, 0, 255), cv2.FILLED)
                # elif lms[0] == 15:
                # ringY = lms[2]
                # cv2.circle(handsFrame, (lms[1], lms[2]), 15, (255, 0, 255), cv2.FILLED)
                elif lms[0] == 19:
                    pinkyX, pinkyY = lms[1], lms[2]
                    # cv2.circle(handsFrame, (lms[1], lms[2]), 15, (255, 0, 255), cv2.FILLED)
                elif lms[0] == 0:
                    handBottomX, handBottomY = lms[1], lms[2]
            if (indexY < handBottomY) and (indexY > indexMid):
                cv2.rectangle(img, (indexX, indexY), (pinkyX, handBottomY), (0, 0, 255), 2)
                # cv2.putText(img, fistWarning, (pinkyX + 2, indexY - 2), (font), .7,
                #           (0, 0, 255), 1, cv2.LINE_4)
            print("Fist")



        return lmList
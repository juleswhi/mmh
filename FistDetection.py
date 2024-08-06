import cv2
import mediapipe as mp
import time
import HandTrackingModule as Htm


def main():
    p_time = 0
    c_time = 0
    cap = cv2.VideoCapture(0)
    detector = Htm.handDetector()

    while True:
        success, img = cap.read()
        _ = detector.findHands(img, draw=False)
        lm_list = detector.findPosition(img)

        c_time = time.time()
        fps = 1/(c_time-p_time)
        p_time = c_time

        # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,0,255), 3)
        cv2.imshow("stream", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()



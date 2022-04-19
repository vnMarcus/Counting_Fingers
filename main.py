import cv2
import time
import os
import mediapipe as mp
import hand as htm



cap=cv2.VideoCapture(0)


FolderPath="Fingers"
lst=os.listdir(FolderPath)
lst_2=[]
for i in lst:
    #print(i)
    image=cv2.imread(f"{FolderPath}/{i}")
    lst_2.append(image)
pTime=0

detector =htm.handDetector(detectionCon=0.55)
fingerid= [4,8,12,16,20]
while True:
    ret,frame =cap.read()
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False)





    if len(lmList) !=0:
        fingers= []
        if lmList[fingerid[0]][1] > lmList[fingerid[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        print(lmList)
        for id in range(1,5):
            if lmList[fingerid[id]][2] < lmList[fingerid[id]-2][2]:
                fingers.append(1)
                print(lmList[fingerid[id]][2])
                print(lmList[fingerid[id]-2][2])
            else:
                fingers.append(0)


        print(fingers)
        songontay=fingers.count(1)
        print(songontay)



        h, w, c = lst_2[songontay - 1].shape
        frame[0:h, 0:w] = lst_2[songontay - 1]

        cv2.rectangle(frame, (0,200), (150,400), (0,255,0), -1)
        cv2.putText(frame, f"{songontay}", (30, 390), cv2.FONT_HERSHEY_PLAIN,10, color=(255,0,0), thickness=3)
    # Viet ra FPS
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    # Show fps
    cv2.putText(frame, f"FPS: {int(fps)}", (150,70), cv2.FONT_HERSHEY_PLAIN, 3, color=(255,0,0), thickness=3)



    cv2.imshow("Dem so ngon tay", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
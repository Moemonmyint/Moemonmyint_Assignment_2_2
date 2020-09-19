import cv2

cap = cv2.VideoCapture(0)
i = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break

    cv2.imshow('hello', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imwrite(str(i) + '.jpg', frame)
    i +=1
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
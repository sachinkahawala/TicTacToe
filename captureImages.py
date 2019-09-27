import cv2
cap = cv2.VideoCapture(1)
count=1
while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    cv2.imwrite('D:/Projects/Tic tac too/images/f'+str(count)+".jpg",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    count+=1
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

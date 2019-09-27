

import sys
import cv2 as cv
import numpy as np
import time
def read(center,radius,image):
    i,j=center
    v=int(radius/(2**0.5))-1
    #print(v)
    mat=image[j-v:j+v+1,i-v:i+v+1]
    #print(mat)
    val=np.mean(np.mean(mat,axis=0),axis=0)
    if val[2]>150:
        return "R"
    elif val[1]>150 and val[0]>150:
        return "G"
    else:
        return " "
def printBoard(board):
        print("-"*13)
        print("|",board[0],"|",board[1],"|",board[2],"|")
        print("-"*13)
        print("|",board[3],"|",board[4],"|",board[5],"|")
        print("-"*13)
        print("|",board[6],"|",board[7],"|",board[8],"|")
        print("-"*13)
    #if val[2]
def markBoard(arr,circleDic,image):
    m2=100000000000
    minI=0
    for x in range(len(arr)):
        v=arr[x][0]**2+arr[x][1]**2
        if v<m2:
            m2=v
            minI=x
    firstrow=[]
    for x in range(len(arr)):
        i,j=arr[x]
        if abs(j-int(arr[minI][1]))<10:
            firstrow.append((i,j))
    firstrow=sorted(firstrow)
    temp1=[]
    for x in range(len(arr)):
        i,j=arr[x]
        if abs(i-int(firstrow[0][0]))<10:
            temp1.append((i,j))
    temp1=sorted(temp1, key=lambda x: x[1])
    secondRow=[]
    for x in range(len(arr)):
        i,j=arr[x]
        if abs(j-int(temp1[1][1]))<10:
            secondRow.append((i,j))
    secondRow=sorted(secondRow)
    thirdRow=[]
    for x in range(len(arr)):
        i,j=arr[x]
        if abs(j-int(temp1[2][1]))<10:
            thirdRow.append((i,j))
    thirdRow=sorted(thirdRow)
    # print(firstrow)
    # print(secondRow)
    # print(thirdRow)
    Board=firstrow+secondRow+thirdRow
    board=list(" "*9)
    for x in range(len(Board)):
        board[x]=read(circleDic[Board[x]]["center"],circleDic[Board[x]]["radius"],image)
    printBoard(board)

def findCircles(src):

    #print(src.shape)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)
    #cv.imshow("gray", gray)


    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=30)
    #print("Houghtransform done")
    circleDic={}
    D=[]
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            circleDic[center]={"center":center}
            D.append(center)
            #print(src[i[1]][i[0]])
            # circle center

            cv.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            circleDic[center]["radius"]=radius
            #print(center)
            #read(center,radius,src)
            cv.circle(src, center, radius, (255, 0, 255), 3)

    markBoard(D,circleDic,src)
    #print(src)
    cv.imshow("detected circles", src)
    #cv.waitKey(0)




    return 0
def findCirclesVideo():
    #frame_rate = 5
    #prev = 0
    cap = cv.VideoCapture(1)#"IMG_9568-c.mp4")

    while(True):
        #time_elapsed = time.time() - prev
        ret, frame = cap.read()

        #frame = cv.resize(frame, (700, 400))
        #print(frame.shape)
        if type(frame)==type(None):
            continue
        cv.waitKey(1000)
        cv.imshow('frame',frame)
        #findCircles(frame)
        try:
            findCircles(frame)
        except Exception as e:
            #print(e)
            continue

        # if time_elapsed > 1./frame_rate:
        #     prev = time.time()
        #     cv.imshow('frame',frame)
        #     try:
        #         findCircles(frame)
        #     except Exception as e:
        #         continue
        #if cv.waitKey(1) & 0xFF == ord('q'):
        #    break
#src = cv.imread("D:/Projects/Tic tac too/f44.jpg")
#findCircles(src)
findCirclesVideo()

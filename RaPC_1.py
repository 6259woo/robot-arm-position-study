#-*- coding: utf-8 -*-
import numpy as np
import math
import cv2

# x = y = l1 = 0P

def distance(x,y):#(0,0)부터 (x,y)까지의 거리
    return math.sqrt(math.pow(x,2) + math.pow(y,2))

def elbow_angle(Distance,l1):#(elbow angle / 2) 반환
    return math.asin((Distance / 2) / l1)

def shoulder_angle(x,y):# x가 0이상일때의 원점(0,0) 부터 (x,y)까지의 각도
    if (x > 0):
        return math.atan(y / x)
    else:#x == 0
        return math.radians(90)

def pos_elbow(Shoulder_angle,Addition_elbow_angle):#elbow 죄표 계산
    y = math.sin(Shoulder_angle + Addition_elbow_angle) * l1
    x = math.cos(Shoulder_angle + Addition_elbow_angle) * l1
    return x,y

def main_cal(x,y,l1):
    if (x < 0):
        print("Overflow<angle>")
    else:
        Distance = distance(x,y)
        if (Distance > (l1 * 2)):
            print("Overflow<distance>")
        else:
            Shoulder_angle = shoulder_angle(x,y)
            Elbow_angle = elbow_angle(Distance,l1)
            Addition_elbow_angle = math.radians(90) - Elbow_angle
            Pos_elbow = pos_elbow(Shoulder_angle,Addition_elbow_angle)

            angle1 = Shoulder_angle + Addition_elbow_angle
            angle2 = Elbow_angle*2

            print("angle1 : {}\tangle2 : {}\tPos_elbow : {}, {}".format(math.degrees(angle1),math.degrees(angle2), Pos_elbow[0], Pos_elbow[1]))

            return angle1, angle2, Pos_elbow[0], Pos_elbow[1]

def img_set(Pos_in_x, Pos_in_y, Pos_elbow_x, Pos_elbow_y):
    img = np.zeros((700,1200,3), np.uint8)

    img = cv2.line(img,(600,650),(600,700),(255,0,0),5)#bootem
    img = cv2.line(img,(0,650),(1200,650),(255,0,0),5)#bootem
    img = cv2.circle(img,(600,650), 30, (0,255,0), 5)#shoulder
    img = cv2.line(img,(600,650),(int(Pos_elbow_x / 2 + 600),(650 - int(Pos_elbow_y / 2))),(0,0,255),5)
    img = cv2.circle(img,(int(Pos_elbow_x / 2 + 600),(650 - int(Pos_elbow_y / 2))), 30, (0,255,0), 5)#elbow
    img = cv2.line(img,(int(Pos_elbow_x / 2 + 600),(650 - int(Pos_elbow_y / 2))),(int(Pos_in_x / 2 + 600),(650 - int(Pos_in_y / 2))),(0,0,255),5)

    return img



# l1 = 600
# Pos_elbow = [0,0]
#
# Pos_in = input("x,y:").split(',')
# Pos_in[0] = float(Pos_in[0])
# Pos_in[1] = float(Pos_in[1])
#
# angle1, angle2, Pos_elbow[0], Pos_elbow[1] = main_cal(Pos_in[0], Pos_in[1], l1)
#
# img = img_set(Pos_in[0], Pos_in[1], Pos_elbow[0], Pos_elbow[1])
#
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

l1 = 600
Pos_elbow = [0,0]
Pos_in = [0,0]
a = 0
img = np.zeros((700,1200,3), np.uint8)


for Pos_in[1] in range(0,1201,100):
    for Pos_in[0] in range(0,1201,100):
        print(Pos_in[0],Pos_in[1])
        try:
            angle1, angle2, Pos_elbow[0], Pos_elbow[1] = main_cal(Pos_in[0], Pos_in[1], l1)
            img = img_set(Pos_in[0], Pos_in[1], Pos_elbow[0], Pos_elbow[1])
        except:
            img = cv2.putText(img, 'ERROR', (10,500), cv2.FONT_HERSHEY_SIMPLEX, 6, (255,255,255), 2)
            print("ERROR")


        cv2.imshow('image', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            a = 1
            break
    if a == 1:
        break

input("끝내려면 엔터")
cv2.destroyAllWindows()

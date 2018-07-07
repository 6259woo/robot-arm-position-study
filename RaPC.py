import numpy as np
import math
import cv2

x=0
y=1
pos_in = input("x,y:").split(',')

l1 = 600

for i in range(0,2):
    pos_in[i] = int(pos_in[i])

distance = math.sqrt(math.pow(pos_in[x],2) + math.pow(pos_in[y],2))

if ((l1 * 2) >= distance):

    perpendicular = math.sqrt(math.pow(l1, 2) - math.pow((distance / 2), 2))
    theta3 =  math.acos(perpendicular/l1)
    theta2 = math.radians(90) - theta3

    # if (pos_in[x] == 0):
    #     theta1 = math.radians(90)
    #     print("angle1: {}\tangle2: {}".format(math.degrees(theta1+theta2),math.degrees(theta3*2)))
    #
    # elif (pos_in[x] > 0):
    #     theta1 = math.atan(pos_in[y]/pos_in[x])
    #     print("angle1: {}\tangle2: {}".format(math.degrees(theta1+theta2),math.degrees(theta3*2)))
    #
    # else:
    #     print("Overflow<angle>")

    if (pos_in[x] < 0):
        print("Overflow<angle>")

    else:
        if (pos_in[x] == 0):
            theta1 = math.radians(90)

        elif (pos_in[x] > 0):
            theta1 = math.atan(pos_in[y]/pos_in[x])

        print("angle1: {}\tangle2: {}".format(math.degrees(theta1+theta2),math.degrees(theta3*2)))

        pos_elbow = [0,0]

        if round((math.degrees(theta1+theta2)), 1) == 180:
            pos_elbow[y] = 0

        else:
            pos_elbow[y] = math.sin(theta1+theta2) * l1

        if round((math.degrees(theta1+theta2)), 1) == 90:
            pos_elbow[x] = 0

        else:
            pos_elbow[x] = math.cos(theta1+theta2) * l1

        print(pos_elbow[x],',',pos_elbow[y])



        img = np.zeros((700,1200,3), np.uint8)

        img = cv2.line(img,(600,650),(600,700),(255,0,0),5)#bootem
        img = cv2.line(img,(0,650),(1200,650),(255,0,0),5)#bootem
        img = cv2.circle(img,(600,650), 30, (0,255,0), 5)#shoulder
        img = cv2.line(img,(600,650),(int(pos_elbow[x] / 2 + 600),(650 - int(pos_elbow[y] / 2))),(0,0,255),5)
        img = cv2.circle(img,(int(pos_elbow[x] / 2 + 600),(650 - int(pos_elbow[y] / 2))), 30, (0,255,0), 5)#elbow
        img = cv2.line(img,(int(pos_elbow[x] / 2 + 600),(650 - int(pos_elbow[y] / 2))),(int(pos_in[x] / 2 + 600),(650 - int(pos_in[y] / 2))),(0,0,255),5)

        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

else:
    print("Overflow<distance>")


# print(pos_in)
# print(type(pos_in[1]))

# print(math.degrees(math.atan(pos_in[y]/pos_in[x])))

# math.radians() / math.degrees(x)

# def a(n):
#     (5 * n**2 + 9) / (2 * n ** 2 + 3*n + 1)
#
# print(a(math.inf))

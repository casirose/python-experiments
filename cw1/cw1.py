# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

up2 = 0
down2 = 0
left2 = 0
right2 = 0

while True:
    up1 = int(input("UP ="))
    down1 =  int(input("down ="))
    left1 = int(input("left = "))
    right1 = int(input("right = "))
    up2 = up2 + up1
    down2 = down2 + down1
    left2 = left2 + left1
    right2 = right2 + right1
    if up1 and down1 and left1 and right1 > 0:
        print("enter zero as value to get out of the loop")  
    else:
        break
            

x2 = up2 - down2
y2 = left2 - right2
x1 = 0
y1 = 0

def distance(up=0,down=0,left=0,right=0):
    distance1 = ((x2-x1)**2 +(y2-y1)**2)**0.5
    print("the distance is ",int(distance1))

distance(up2,down2,left2,right2)

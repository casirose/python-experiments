a=0
b=0
while True:
   r = input("enter the direction step: ")
   try:

    if not r:
        break
    dire, steps = r.split(' ')
    steps = int(steps)
    if dire == "left":
        a -=  steps
    elif dire == "right":
        a +=  steps
    elif dire == "up":
        b +=  steps
    elif dire == "down":
        b -=  steps
    else:
        pass
   
   except ValueError:
        print("please Enter the DIRECTION and the INDEX in INTERGER TYPE")
distance = (a**2 + b**2)**(1/2)
print("the output is: ",int(distance))
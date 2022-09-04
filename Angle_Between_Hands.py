t=input()
h=((ord(t[0])-48)*10+ord(t[1])-48)
m=((ord(t[3])-48)*10+ord(t[4])-48)
angle=(11*(m/2)-(30*h))

if angle<0:
    angle+=360
if angle >180:
    angle = 360-angle
print(angle)
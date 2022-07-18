import math
x,y,z=map(int,input().split())
f=math.pow(x,y)%z
print(int(f))
n = int(input())

x = [0,1]

a = 0
b = 1

count=0
for i in range(n):
    c = a+b
    x.append(c)
    if c>n:
        break
    a=b
    b=c
after  = x[len(x)-1]
before = x[len(x)-2]

daff = after-n
dbeff = n-before

if daff == dbeff:
    print(before,after)
elif daff>dbeff:
    print(before)
else:
    print(after)
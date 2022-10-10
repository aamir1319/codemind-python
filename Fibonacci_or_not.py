n = int(input())

arr = [0]
a,b=0,1
for i in range(n//2):
    arr.append(a+b)
    a,b=b,a+b

if n in arr:
    print('True')
else:
    print('False')
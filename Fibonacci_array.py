n = int(input())
x = list(map(int,input().split()))

f =0
for i in range(2,n):
    if x[i-2]+x[i-1]!=x[i]:
        f=0
        break
    else:
        f=1
if bool(f):
    print('yes')
else:
    print('no')
a = int(input())
x = list(map(int,input().split()))
# print(x)
osum,esum=0,0

for i in range(a):
    if i==0 or i%2==0:
        esum+=x[i]
    else:
        osum+=x[i]
# print(esum,osum)
if (osum-esum)==0:
    print('YES')
else:
    print('NO')
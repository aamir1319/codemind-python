osum=0
esum=0
n = int(input())
x = list(map(int,input().split()))

for i in range(n):
    if i==0:
        esum+=x[i]
    elif i%2==0:
        esum+=x[i]
    else:
        osum+=x[i]
        
print(max(esum,osum)-min(esum,osum))
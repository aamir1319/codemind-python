n = int(input())
x = list(map(int,input().split()))
temp=[]
for i in range(n//2+1):
    temp.append(x[i])
    temp.append(x[-(i+1)])

if n%2==0:
    temp.pop()
    temp.pop()
else:
    temp.pop()
for i in temp:
        print(i,end=' ')

if n%2==1:
    print(0)
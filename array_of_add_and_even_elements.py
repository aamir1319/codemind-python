n = int(input())
x = list(map(int,input().split()))

for i in x:
    if i%2==1:
        print(i,end=' ')
for i in x:
    if i%2==0:
        print(i,end=' ')
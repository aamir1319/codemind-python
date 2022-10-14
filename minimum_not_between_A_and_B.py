n = int(input())
x = list(map(int,input().split()))
a,b= map(int,input().split())
temp = []
for i in x:
    if i<a or i>b:
        temp.append(i)
if not bool(len(temp)):
    print(-1)
else:
    print(min(temp))
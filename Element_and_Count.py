n = int(input())

x = list(map(int,input().split()))
temp = []
for i in x:
    if i not in temp:
        temp.append(i)
        print(i,x.count(i),end=' ')
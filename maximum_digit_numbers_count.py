n = int(input())

x= list(map(int,input().split()))

max = 0
for i in x:
    if max<len(list(str(i))):
        max = len(list(str(i)))

for i in x:
    if max==len(list(str(i))):
        print(i,end=' ')
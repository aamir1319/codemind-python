n = int(input())
x = list(map(int,input().split()))

temp = []
for i in x:
    if i%2==1 and i not in temp:
        temp.append(i)
print(len(temp))
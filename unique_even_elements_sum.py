n = int(input())
x = list(map(int,input().split()))
s=0
temp = []
for i in x:
    if i%2==0 and i not in temp:
        temp.append(i)
        s+=i
print(s)
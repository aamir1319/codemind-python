x = int(input())
t = 0
# print(temp)
for i in range(x):
    s = input()
    if '+' in s:
        t+=1
    elif '-' in s:
        t-=1
print(t)
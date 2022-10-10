n = int(input())
x = list(map(int,input().split()))

unq = []

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        elif x[i]==x[j]:
            break
    else:
        unq.append(x[i])
if len(unq)==0:
    print(-1)
else:
    max_ = 0
    for i in unq:
        if i>max_:
            max_=i
    print(max_)
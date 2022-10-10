a= int(input())
x = list(map(int,input().split()))
res = []
flag=1
for i in range(a):
    for j in range(a):
        if i==j:
            continue
        elif x[i]==x[j]:
            flag=0
            break
    else:
        flag=1
    if flag==1:
        res.append(x[i])
if len(res)==0:
    print(-1)
else:
    for i in res:
        print(i,end=' ')
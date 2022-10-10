t = int(input())
for i in range(t):
    x = list(input())
    a,b=int(min(x)),int(max(x))
    flag=0
    for i in range(a,b+1):
        if str(i) not in x:
            print('NO')
            break
    else:
        print('YES')
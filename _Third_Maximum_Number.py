n = int(input())
x = list(map(int,input().split()))

m  = max(x)
mi = min(x)
mc = 1

for i in range(m-1,mi-1,-1):
    if i in x:
        mc+=1
        if mc==3:
            print(i)
            break
else:
    print(m)
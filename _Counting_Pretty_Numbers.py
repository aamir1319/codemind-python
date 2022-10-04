t = int(input())

for i in range(t):
    x= list(map(int,input().split()))
    count=0
    for j in range(x[0],x[1]+1):
        if (j%10==2 or j%10==3 or j%10==9):
            count+=1
    print(count)
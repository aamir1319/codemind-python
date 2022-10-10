a = int(input())
x = list(map(int,input().split()))

for i in range(a):
    count=0
    for j in range(a):
        if j!=i and x[i]>x[j]:
            count+=1
    print(count,end=' ')
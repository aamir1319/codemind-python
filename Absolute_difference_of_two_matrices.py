n= int(input())

m1 = []
m2 = []
for i in range(n):
    m1.append(list(map(int,input().split())))
for i in range(n):
    m2.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if j==n-1:
            print(abs(m1[i][j]-m2[i][j]))
        else:
            print(abs(m1[i][j]-m2[i][j]),end=' ')
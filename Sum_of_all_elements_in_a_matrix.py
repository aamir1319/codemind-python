n,m = map(int,input().split())
s=0
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        s+=mat[i][j]
print(s)
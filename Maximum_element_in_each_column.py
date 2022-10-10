m,n = map(int,input().split())

mat  = []

for i in range(m):
    mat.append(list(map(int,input().split())))
j=0
while j!=n:
    max_ = 0
    for i in range(m):
        if mat[i][j]>max_:
            max_ = mat[i][j]
    print(max_)
    j+=1
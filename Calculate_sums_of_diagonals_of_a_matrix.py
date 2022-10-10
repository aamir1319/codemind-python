n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))
    
pd = 0
sd = 0

for i in range(n):
    for j in range(n):
        # print(str(i)+str(j),end=' ')
        if i==j:
            pd+=mat[i][j]
        if (i+j)==n-1:
            sd+=mat[i][j]
            # print(i,j)
    # print()
# print(mat)          
print('Principal Diagonal:'+str(pd))
print('Secondary Diagonal:'+str(sd))
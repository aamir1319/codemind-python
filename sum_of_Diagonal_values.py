n,m=map(int,input().split())
mat=[]
s=0
for i in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
for i in range(n):
    for j in range(m):
        if i==j:
            s+=mat[i][j]
        elif i+j==n-1:
            s+=mat[i][j]
            
            
            
print(s)            
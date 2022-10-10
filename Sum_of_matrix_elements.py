m = int(input())
n = int(input())
mat = []
for i in range(m):
    t = list(map(int,input().split()))
    mat.append(t)
# print(mat)
sum=0
for i in range(m):
    for j in range(n):
        sum+= mat[i][j]
print(sum)
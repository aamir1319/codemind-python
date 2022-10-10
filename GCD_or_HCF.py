x = list(map(int,input().split()))

max_ = 0

if x[0]>x[1]:
    max_ = x[0]+1
else:
    max_ = x[1]+1
hcf = 0
for i in range(1,max_):
    if x[0]%i==0 and x[1]%i==0:
        hcf = i
print(hcf)
x = list(map(int,input().split()))

if x[0]>x[1]:
    max_ = x[0]
else:
    max_ = x[1]

for i in range(1,max_):
    if x[0]%i==0 and x[1]%i==0:
        hcf = i

lcm = (x[0]*x[1])/hcf
print(int(lcm))
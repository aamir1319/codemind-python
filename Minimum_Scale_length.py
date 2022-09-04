def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
n=int(input())
x=list(map(int,input().split()))
hcf=gcd(x[0],x[1])
for i in range(1,n):
    hcf=gcd(hcf,x[i])
print(hcf)    
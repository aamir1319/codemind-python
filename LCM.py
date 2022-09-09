a,b=map(int,input().split())
hcf=0
h=max(a,b)
for i in range(1,h+1):
    if a%i==0 and b%i==0:
        hcf=i
print((a*b)//hcf)        
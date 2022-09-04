def lcm(a,b):
    m=max(a,b)
    while True:
        if m%a==0 and m%b==0:
            return m
        else:
            m+=max(a,b)
n=int(input())
a=list(map(int,input().split()))
ans=lcm(a[0],a[1])
for i in range(1,n):
    ans=lcm(ans,a[i])
print(ans)    
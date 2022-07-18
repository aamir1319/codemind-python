n,r=map(int,input().split())
for i in range(r+1):
    if i%2!=0:
        k=n*i
        print(n,"x",i,"=",k)
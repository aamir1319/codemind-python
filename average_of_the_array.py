n=int(input())
x=list(map(int,input().split()))
k=sum(x)
avg=k/n
print("{:.2f}".format(avg))
a,b,c=map(int,input().split())
s=(a+b+c)/2
n=s*(s-a)*(s-b)*(s-c)
print("{:.2f}".format((n)**0.5))

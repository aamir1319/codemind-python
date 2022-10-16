def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return (a*b)/gcd(a,b)






for i in range(int(input())):
    n,a,b,k=map(int,input().split())
    x=n/a
    y=n/b
    z=n/lcm(a,b)
    if(x+y-2*z)>=k:
        print("Win")
    else:
        print("Lose")
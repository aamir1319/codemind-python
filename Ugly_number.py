def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
pr1=[]
for i in range(2,n+1):
    if n%i==0 and prime(i):
        pr1.append(i)
if (2 in pr1 or 3 in pr1 or 5 in pr1):
    print("Ugly Number")
elif n==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")
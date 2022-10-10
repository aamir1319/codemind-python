def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

a = int(input())
flag=0
for i in range(2,a):
    for j in range(2,a):
        # print(i,j,prime(i)and prime(j))
        if prime(i) and prime(j):
            if (i*j)==a:
                print(i,j)
                flag=1
                break
        else:
            flag=0
    if flag==1:
        break
else:
    print(-1)
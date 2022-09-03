n=int(input())
while(n!=0):
    r=n%10
    n//=10
    if (r%2==0) and (n%2==0):
        print("Even")
        break
    elif(r%2!=0) and (n%2!=0):
        print("Odd")
        break
    else:
        print("Mixed")
        break
    

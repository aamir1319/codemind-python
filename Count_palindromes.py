def palindrome(n):
    temp = n
    rev = 0
    while temp:
        rev = rev*10 + temp%10
        temp//=10
    if rev==n:
        return True
    else:
        return False

n = int(input())

x = list(map(int,input().split()))

c=0
for i in x:
    if palindrome(i):
        c+=1
print(c)
def reve(n):
    rev = 0
    while n:
        rev = rev*10 + n%10
        n//=10
    return rev
    
def palin(n):
    if reve(n)==n:
        return True
    return False


x = int(input())

while True:
    x+=reve(x)
    if palin(x):
        break
print(x)
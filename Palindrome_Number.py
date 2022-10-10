for i in range(int(input())):
    a = int(input())
    temp =a
    rev = 0
    while temp:
        rev = rev*10 + temp%10
        temp//=10
    print(rev==a)
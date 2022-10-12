for i in range(int(input())):
    a = int(input())
    b = bin(a)
    b = list(b)
    for i in range(2,len(b)):
        print(b[i],end='')
    print()
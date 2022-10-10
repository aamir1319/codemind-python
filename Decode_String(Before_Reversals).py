for i in range(int(input())):
    a,b = map(int,input().split())
    s = input()
    while b:
        s1 = s[:b]
        s1 = s1[::-1]
        s2 = s[b:]
        s = s1+s2
        b-=1
    print(s)
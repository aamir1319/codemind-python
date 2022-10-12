for i in range(int(input())):
    a = list(input())
    pw = len(a)-1
    s = 0
    for i in a:
        s += int(i)*(2**pw)
        pw-=1
    print(s)
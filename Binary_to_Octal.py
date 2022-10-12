for i in range(int(input())):
    s = list(input())
    dec = 0
    pw = len(s)-1
    for i in s:
        dec = dec + int(i)*(2**pw)
        pw-=1
    print(oct(dec).replace('0o',''))
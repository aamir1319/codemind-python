n=int(input())
h="0123456789"
for i in range(n):
    m=input()
    if m.isdecimal():
        print(True)
    else:
        print(False)
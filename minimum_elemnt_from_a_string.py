s = input().split()
s = s[-1]
ms = min(s)
if ms.isupper():
    if ms.lower() in s:
        print(ms.lower())
    else:
        print(ms)
else:
    print(ms)

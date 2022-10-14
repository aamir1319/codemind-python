s = input().split()
ns = 0
ms = 0
for i in s:
    ns+=ord(min(i))
    ms+=ord(max(i))
print(abs(ns-ms))
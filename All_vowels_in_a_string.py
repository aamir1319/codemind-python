s = input()

v = ['a','e','i','o','u']
V = ['A','E','I','O','U']

c= 1
for i in v:
    if i not in s:
        c=0
        break
if c==0:
    for i in V:
        if i not in s:
            c=0
            break
    else:
        c=1
print(bool(c))
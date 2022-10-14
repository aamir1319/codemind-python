s = input().split()

v = ['a','e','i','o','u']

for i in s:
    c =0
    for j in i:
        if j in v:
            c+=1
    print(c,end=' ')
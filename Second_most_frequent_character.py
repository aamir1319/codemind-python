s = input()
d = {}
for i in s:
    d[i] = s.count(i)

md = max(d.values())
f=0
for i in range(md-1,-1,-1):
    for key,val in d.items():
        if val==i:
            print(key)
            f=1
            break
    if f==1:
        break
else:
    print(-1)
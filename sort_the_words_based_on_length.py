s = input().split()

d = {}
for i in s:
    d[len(i)] = []
for i in s:
    d[len(i)].append(i)

for i in sorted(d.keys()):
    for j in sorted(d[i]):
        print(j,end=' ')
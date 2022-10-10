from itertools import product

n = int(input())
l = list(product([0,1],repeat=n))

for i in range(len(l)):
    for j in l[i]:
        print(j,end='')
    print()
a = list(input())

for i in range(len(a)):
    if a[i]=='6':
        a[i]='9'
        break

for i in a:
    print(i,end='')
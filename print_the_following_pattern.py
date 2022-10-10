a = int(input())

b=a-1

for i in range(a):
    for j in range(a):
        if i==j or j==b:
            print('x',end='')
        else:
            print('0',end='')
        
    print()
    b-=1
n = int(input())

a = n+ 64

for i in range(a,64,-1):
    for j in range(64,i):
        print(chr(i),end=' ') 
    print()
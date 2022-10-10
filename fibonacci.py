a = 0
b =1
print(a,b,end= ' ')
for i in range(int(input())-2):
    print(a+b,end=' ')
    a,b = b,a+b
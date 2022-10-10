n=input()
k=int(n)*int(n)
for i in n:
    if n in str(k):
        print('Automorphic Number')
        break
else:
    print('Not an Automorphic Number')
n=input()
for i in n:
    if n.count(i)!=1:
        print(False)
        break
else:
    print(True)
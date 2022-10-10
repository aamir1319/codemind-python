n=list(input())
# print(n)
for i in n:
    # print(i)
    if n.count(i)!=1:
        # print(i)
        print("Not Unique Number")
        break
        
else:
    print("Unique Number")
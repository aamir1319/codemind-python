n = int(input())

x = list(map(int,input().split()))
ecount =0
ocount =0
for i in x:
    if i%2==0:
        ecount+=1
    else:
        ocount+=1
print(ecount,ocount)
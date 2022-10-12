a,b = map(int,input().split())

if (a+1==b) or (b+1==a) or (a==10 and b==1) or (a-1==b) or (b-1==a) or (b==10 and a==1): 
    print('Yes')
else:
    print('No')
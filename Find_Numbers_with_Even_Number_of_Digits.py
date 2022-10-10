a = int(input())
count =0 
x = list(map(int,input().split()))

for i in range(a):
    if (len(str(x[i])))%2==0:
        count+=1
print(count)
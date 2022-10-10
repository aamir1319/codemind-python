n = int(input())
nums = list(map(int,input().split()))
m = int(input())

x = list(map(int,input().split()))

target = []
for i in range(n):
    target.insert(x[i],nums[i])
for i in target:
    print(i,end= ' ')
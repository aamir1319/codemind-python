def very_big_sum(x):
    sum = 0
    for i in x:
        sum+=i
    return sum
n = int(input())
x = list(map(int,input().split()))

print(very_big_sum(x))
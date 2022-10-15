def square(n):
    for i in range(n//2):
        if i*i==n:
            return True
    return False

n = int(input())

print(square(n))
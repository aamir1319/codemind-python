s = input()
sum_ = 0
for i in s:
    if i.isdigit():
        sum_+=int(i)
print(sum_)
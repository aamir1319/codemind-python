s = input()
sc = "~`!@#$%^&*()_-+={}[]|\:;'/?><,."
c=0
for i in s:
    if i in sc:
        c+=1
print(c)
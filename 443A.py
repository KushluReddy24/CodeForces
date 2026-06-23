n=input()
k=""
for i in n:
    if i.isalpha():
        k+=i
print(len(set(k)))

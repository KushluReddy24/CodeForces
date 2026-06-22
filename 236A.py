n=input()
k=[]
for i in n:
    k.append(i)
k=set(k)
if len(k)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

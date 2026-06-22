n=input().split()
n_1=int(n[0])
n_2=int(n[1])
k=input().split()
p=0
for j in range(n_1):
    if int(k[j])>=int(k[n_2-1]) and int(k[j])>0:
        p+=1
print(p)

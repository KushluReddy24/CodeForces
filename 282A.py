n=int(input())
k=0
for i in range(n):
    l=input()
    if "+" in l:
        k+=1
    else:
        k-=1
print(k)
    

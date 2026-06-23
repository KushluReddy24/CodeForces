n=int(input())
k=input()
count=0
for i in range(1,n):
    if k[i]==k[i-1]:
        count+=1
print(count)

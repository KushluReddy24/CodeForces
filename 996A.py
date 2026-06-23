n=int(input())
count=0
for i in [100,20,10,5,1]:
  count+=n//i
  n%=i
print(count)

n=int(input())
cap=0
maxi=0
for i in range(n):
  o,i=map(int,input().split())
  cap=cap-o+i
  maxi=max(cap,maxi)
print(maxi)

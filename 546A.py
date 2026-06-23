k,n,w=map(int,input().split())
money_needed=k*(w*(w+1))//2
if n<money_needed:
  print(money_needed-n)
else:
  print(0)

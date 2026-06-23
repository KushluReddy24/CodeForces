n=int(input())
p=""
for i in range(n):
  if i%2==0:
    q="I hate"
  else:
    q="I love"
  if i<n-1:
      btw="that"
  else:
      btw="it"
  p+=q+" "+btw+" "
print(p)
  

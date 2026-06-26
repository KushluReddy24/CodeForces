n=input().split()
k2=int(n[0])
k3=int(n[1])
k5=int(n[2])
k6=int(n[3])

p=min(k2,k5,k6)
l=min(k2-p,k3)
print(256*p+l*32)

n=input()
upper_count=0
lower_count=0
for i in n:
    if i==i.upper():
        upper_count+=1
    else:
        lower_count+=1
if upper_count>lower_count:
    print(n.upper())
else:
    print(n.lower())
    

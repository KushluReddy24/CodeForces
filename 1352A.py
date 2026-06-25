n=int(input())

for i in range(n):
    k=input()
    
    l=[]
    for i in range(len(k)):
        if k[i]!="0":
            new_num=int(k[i])*(10**int(len(k)-i-1))
            l.append(str(new_num))
           
    print(len(l))
    print(" ".join(l))
    

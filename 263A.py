for i in range(5):
    n=input().split()
    for j in range(5):
        if n[j]=="1":
            print(abs(i-2)+abs(j-2))

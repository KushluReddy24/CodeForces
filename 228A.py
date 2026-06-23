n=input().split()
if len(n)==len(set(n)):
    print(0)
else:
    print(len(n)-len(set(n))

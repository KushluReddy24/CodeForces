year=int(input())
while True:
    year+=1
    year=str(year)
    
    if len(year)==len(set(year)):
        print(year)

        break

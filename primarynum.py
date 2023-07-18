j= 2
flage = 0
for x in range(3,101):
    while j<=x:
        if x % j == 0:
            flage+=1
        j+=1
    if flage == 1:
        print(x, "is prime")
    flage = 0
    j = 2




    
print("dsfsfs")
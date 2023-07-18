import array
# from import array *


"""input = int(input("enter a m value"))"""
a = [[10, 6, 8],
    [7, 9, 6],
    [9, 6, 8]]

b = [[11, 2, 8],
    [7, 9, 6],
    [9, 6, 8]]
c = []


#1st question c+c

# for x in range(0, len(a)):
#     k =[]
#     for i in range(0,len(b)):
#         sum = a[x][i]+b[x][i]
#         k.append(sum)
#     c.append(k)
        
# print(c)    

#2nd question r+c
"""
for x in range(0, len(a)):
    k =[]
    for i in range(0,len(b)):
        sum = a[x][i]+b[i][x]
        k.append(sum)
    c.append(k)
        
print(c)    
"""



#3rd question
m = []
for x in range(0, len(a)):
    k =[]
    for i in range(0,len(b)):
        sum = a[x][i]*b[i][x]
        for m in range(0, len(m)):
            sum2 = a[x][i]+b[i][x]
        k.append(sum)
    c.append(k)
        
print(c)    
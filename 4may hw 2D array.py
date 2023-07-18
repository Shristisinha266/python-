import array as array
"""
ad = ("i",[[86, 6, 54], [54, 65, 4]])

for x in ad:
    for y in x:
        print(y, end=" ")
    print()"""

ar = [2,3,4,5,6]
factArray = [1] * len(ar)
print(factArray)
for y in range(0, len(ar)):
    #fact = 1
    for x in range(1, ar[y]+1):
        #fact = fact * x
        factArray[y] = factArray[y] * x
    #factArray[y]=fact

for elem in factArray:
    print(elem , end=" ")

# one = arr.array("i", [23, 5, 2, 5, 223, 5])
# # print(len(one))
# two = arr.array("i", [])
# length = len(one)
# for i in range(length):
#     if one[i]%2 != 0:
        
    #     # print(i)l
    #     # print(i, ":Before One is: ", one)
    #     # print(i, ":Before Two is: ", two)
        # two.append(one[i])
        # one.pop(one[i])
        # print(i)
    #     print(i, ":A")                                                                                  
        #length -=1
        # print(i, ": One is: ", one)
        # print(i, ": Two is: ", two)
    # print(one[i], end=" ")

# for x in one:
#     if x%2 == 0:
#         print(one)
#     else:
#         two.append(x)
#         one.remove(x)


# print(223%2)import array
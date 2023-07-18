"""import array
marks = array.array("i",[10, 20, 40, 70])
 
for x in marks:
    print(x)
#Question -1
a = len(marks)
n = 0 
while(n<a):
    print(marks[n])
    n+=1
    
"""


from array import*
marks = array("i",[10, 20, 40, 70, 0, 0])
"""
# for x in marks:
#     print(x)
a = len(marks)
n = 0 
while(n<a):
    print(marks[n])
    n+=1
"""

#remove given value
n=0
while n in marks:
    marks.remove(n)
    print(n)

print("after delete",marks) 

"""
marks = array("i",[])
while True:
    val = int(input("enter a value"))
    
    if val == 0:
        break
    marks.append(val)
    
print(marks)
"""
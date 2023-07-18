print("Hello world")

#Q-1
"""empdetail = {}
empdetail["name"] = "shristi"
empdetail["city"] = "delhi"
empdetail["dep"] = "sales"
empdetail["salary"] = 5000
empdetail["DOB"] = "2may 2004"
print(empdetail)"""



#Q-2
"""
str = input("enter your text")
dict={}
for x in str:
    if x in dict:
        dict[x]+=1
    else:
       dict[x] = 1
print(dict)
"""

#Q-3
D = {}
n = int(input("how many employes Would you want to add"))
for x in range(n):
  ename = input("employer name")
  esal = int(input("salary of employee"))
  D[ename] = esal
print("Created dictionry")
print(D)
var = input("enter exist emloye")
print(D[var])

# remove = D.pop(D[var])
# print(remove)

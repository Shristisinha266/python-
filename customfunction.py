
#isdigit
"""str = "sdjsadhajah673173"

print(str.isdigit())
"""
#isdecimal
"""
str = "35.3"

print(str.isdecimal())

"""

#isspace
"""
str = " sd sdsd"
print(str.isspace())

#count
str = " sd sdsd"
print(str.count(" "))
"""

#title
"""
str = "hello i am here"
print(str.title())
"""

#istitle
"""
str = "Hello I Am Here"
print(str.istitle())
"""
#join
"""
str = "hello"
print(str.join(str))
"""
"""
#partisan
str = "hajhajah"
print(str.partition('j'))

"""

"""
#ljust
str = "ajhdajdhajd"
print(str.ljust(30),"hello")

"""

#rjust
"""
str = "ajhdajdhajd"
print(str.rjust(30),"hello")
"""

"""

def one(text, sufix):
    if text in sufix:
      return print("ok we get it")
    # else:
    #   print("no we have not")
print(one("how are you","you"))
    
"""

"""
def ncapital(name):
    return(name.capitalize())
print(ncapital("shristi"))


char = "a"
print(ord(char))

ascii = 97
print(chr(ascii))
"""
"""
str = "Ane"
if ord(str)>97:
    print("ok")
else:
    print("not")

"""
"""
str = "sSs"
for x in str:
    if ord(x)<90:
        print("True")
    # else:
    #     print("false")
    
"""



"""
# rjust function
def rightjust(x, y, z):
    lenth = len(x)
    for y in range(y-lenth):
        x+=z
    return(x)

a = "hello"
print(rightjust(a,8,"-"))


"""
"""def space(x):
    z =""
    for y in x:
        if y !=" ":
            z+=y
    return(z)
print(space("gfjg hfdjk  fhgjk"))"""
"""
#isupper function
def thisupper(x):
    for z in x:
        u = 0
        if ord(z)<97:
            u+=1
    if u >= 1:
        print("false")
    else:
        print("true")

print(thisupper("helLo"))"""

"""def cswapcase(x):
    c=""
    for y in x:
        a = ord(y)   
        if a <=122 and a>=97:
            a = a-32
            c += chr(a)
        else:
            a = a+32
            c += chr(a)
    return(c)
    
print(cswapcase("hjsdajkJHKLJKHJKLHKJ"))
"""
"""# capital each word que 2
def cswapcase(x):
    c=""
    for y in x:
        a = ord(y)   
        if a <=122 and a>=97:
            a = a-32
            c += chr(a)
        else:
            c += chr(a)
    return(c)
print(cswapcase("jkHdj"))"""

"""
# Q-8
def occurance(string, fl):
    count = 0
    for x in range(len(string)):
        if(string[x]==fl):
            count= count+1
    return (count)
print(occurance("shristi","h"))
    


"""

"""
def title(str):
    i=0
    for x in range(len(str)):
        a = ord(str)
        if a == 32:
          """




"""

str = "jhasdajhd713971239jyadj999adhad"
c = []
for x in range(len(str)):
    # print(x, end=" ")
    if str[x]==1 or str[x]==2 or str[x]==3 or str[x]==4 or str[x]==5 or str[x]==6 or str[x]==7 or str[x]==8 or str[x]==9 or str[x]==0 and len(str)==3:
        c.append(str[x])
    print(c)

"""



"""str = "jhasdajhd713971239jyadj999adhad"
c = []
for x in range(len(str)):
    # print(x, end=" ")
    if filter(x.isdigit(), str) and len(str)==3:
        c.append(str[x])
    print(c)"""



from collections import Counter
def solve(s):
   d = Counter(s)
   for k in d:
      d[k] -= 2
      if all(d[i] % 3 == 0 for i in d):
         return True
      d[k] += 2
   return False

s = "22sfsf53"
print(solve(s))



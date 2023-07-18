"""x = input("Enter here first number")
z = input("please select any of these symols +, - , /, //, **, %")
y = input("Enter here second number")

#print (int(x)+int(y))


if z=="+":
    print (int(x)+int(y))
elif(z=="-"):
    print (int(x)-int(y))
elif(z=="/"):
    print (int(x)/int(y))
elif(z=="**"):
    print (int(x)**int(y))
elif(z=="//"):
    print (int(x)//int(y))
elif(z=="%"):
    print (int(x)%int(y))
else:
    print("simbloe is undefine")
"""


#assignment 12

'''
def sal(sl):
    #this is hra
    if sl>3000:
        hra = sl*30/100
    elif sl>1000:
        hra = sl*25/100
    else:
        hra = sl*20/100
    
    # da
    da = sl*30/100

    # ca
    if sl>2000:
        ca = 100
    elif sl>1000:
        ca =75
    else:
        ca =50
    
    # ea
    if sl>1000:
        ea = 100
    else:
        ea = 0
        
    # deducation
    
    # pf
    pf = sl*6/100
    
    # gip
    if sl>3000:
        gip = 80
    elif sl>1000:
        gip = 60
    else:
        gip = 40
    bas = hra+da+ca+ea+sl
    ded  =pf+gip
    print("your salary slip")
    print("your hra is", hra)
    print("your da is", da)
    print("your ca is", ca)
    print("your ea is", ea, end="\n \n ")
    print("your salary deduction")
    print("your pf is", pf)
    print("your gip is", gip, end=" \n \n")
    print("your gross salary basic+hra+da+ca+ea+ :", hra+da+ca+ea+sl)
    print("Total deducation gip+pf", gip+pf)
    print("net salary gross-deducation", bas-ded)
    
    
    
salary = int(input("enter your salary"))
sal(salary)
'''






def generate_s_pattern(size):
    for row in range(size):
        for col in range(size):
            if row == 0 or row == size - 1 or row == size // 2:
                print('*', end=' ')
            elif row < size // 2 and col == 0:
                print('*', end=' ')
            elif row > size // 2 and col == size - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

# Example usage
pattern_size = 7  # Adjust the size of the pattern as needed
generate_s_pattern(pattern_size)



def print_pattern_R():
    for row in range(7):
        for col in range(7):
            if col == 0 or ((row == 0 or row == 3) and col < 6) or (col == 6 and row != 0 and row != 3):
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Call the function to print the pattern
print_pattern_R()
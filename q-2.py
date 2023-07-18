inp_str = "jasdhkah999dajkdh 2384928497832h sjfwhsdf897wsdrt983i54390583jfkxdhf9e78593589"

 
print("Original String : " + inp_str) 
num = ""
for c in inp_str:
    x  = c.isdigit()
    if len(x) ==3:
        num = num + c
print("Extracted numbers from the list : " + num) 



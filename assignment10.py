
age = 40
rt = "ac"
td = 10
acrc = 500
grc = 200
if td >=10 and age >=60:
    if rt=="ac":
        print(td*acrc - 2*acrc)
    elif rt=="gen":
        print(td*grc - 2*grc)
elif td <=10 and age >=60:
    if rt=="ac":
        print(td*acrc - 1*acrc)
    elif rt=="gen":
        print(td*grc - 1*grc)
elif td >=10 and age < 60:
    if rt=="ac":
        print(td*acrc - 1*acrc)
    elif rt == "gen":
        print(td*grc-1*grc)
elif td <10 and age <60:
    print("not dis")

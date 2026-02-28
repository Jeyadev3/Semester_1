n=input("Enter a string :")
for i in n:
    if i.isalpha() or i.isspace():
        print(i,end="")

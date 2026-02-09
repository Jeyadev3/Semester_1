def show_menu(menu):
    for i,j in menu.items():
        print(i,":",j)

def order(menu,ord):
    while True:
        o=input("Enter the order :")
        if o in menu:
            ord.append(o)
        else:
            print("Not available")
        a=input("do u want more(Y/N) :")
        if a=="N":
            break

def bill(ord,menu):
    su=[]
    for i in ord:
        x=menu[i]
        su.append(x)
    s=sum(su)
    return s

def discount(s,ord):
    discount=0
    if "a" in ord:
        discount+=2
    if s>20:
        discount+=3
    print("Total discount is ",discount," and total bill is ",s-discount)
            
menu={}
n=int(input("Enter the no of values :"))
for i in range(n):
    m=input("Enter the name of food :")
    f=float(input("Enter the price :"))
    menu[m]=f
print(menu)
        
show_menu(menu)

ord=[]
order(menu,ord)
print(ord)

s=bill(ord,menu)
print("Total bill is ",s)

discount(s,ord)

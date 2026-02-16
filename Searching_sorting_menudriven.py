'''Q1.
products=[
    {"id":101,"name":"laptop","price":900,"stock":12},
    {"id":205,"name":"keyboard","price":25,"stock":85},
    {"id":150,"name":"monitor","price":180,"stock":30}
]

def bubble(products):
    n=len(products)
    for i in range(n-1,0,-1):
        for j in range(i):
            if products[j]["price"]>products[j+1]["price"]:
                products[j],products[j+1]=products[j+1],products[j]
    return products

def selection(products):
    n = len(products)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if products[j]["stock"] > products[max_index]["stock"]:
                max_index = j
        products[i], products[max_index] = products[max_index], products[i]
    return products

def insertion(products):
    for i in range(1,len(products)):
        key=products[i]
        j=i-1
        while j>=0 and products[j]["name"]>key["name"]:
            products[j+1]=products[j]
            j-=1
        products[j+1]=key
    return products

print(bubble(products))
print(selection(products))
print(insertion(products))

def binary(products,n):
    u=len(products)-1
    l=0
    while u>=l:
        m=(u+l)//2
        if products[m]["id"]==n:
            return products[m]
        else:
            if products[m]["id"]<n:
                l=m+1
            else:
                u=m-1
    return -1

def linear(products,name):
    for i in range(len(products)):
        if products[i]["name"]==name:
            return products[i]
    return("not found")

def func(min,max,products):
    result=[]
    for i in range(len(products)):
        if products[i]["price"]>min and products[i]["price"]<max:
            result.append(products[i])
    return result

n=int(input("Enter the number to search :"))
print(binary(products,n))   
name=input("Enter the name to search :")
print(linear(products,name))
min=int(input("Enter the lower bound :"))
max=int(input("Enter the upper bound :"))
print(func(min,max,products))
'''

books=[{"title":"The Hobbit","author":"Tolkein","year":1937},
       {"title":"Harry Potter","author":"J.K.Rowling","year":2000},
       {"title":"The Alchemist","author":"Paulo Coelho","year":1988}]

def bubble(books):
    n=len(books)
    for i in range(n-1,0,-1):
        for j in range(i):
            if books[j]["title"]>books[j+1]["title"]:
                books[j],books[j+1] = books[j+1],books[j]
    return books

def selection(books):
    n=len(books)
    for i in range(n-1):
        for j in range(i+1,n):
            if books[i]["author"]>books[j]["author"]:
                books[i],books[j]=books[j],books[i]
    return books

def insertion(books):
    for i in range(1,len(books)):
        key=books[i]
        j=i-1
        while j>=0 and books[j]["year"]>key["year"]:
            books[j+1]=books[j]
            j-=1
        books[j+1]=key
    return books



print(bubble(books))
print(selection(books))
print(insertion(books))
           
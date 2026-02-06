def perfect(n):
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    print(l)
    s=sum(l)
    if s==n:
        return("The number is a perfect number")
    else:
        return("The number is not a perfect number")
n=int(input("Enter the number to check :"))
l=[]
p=perfect(n)
print(p)

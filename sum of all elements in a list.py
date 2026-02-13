n=int(input("Enter n :"))
sum=0
elements=input("Enter the elements :")
s=elements.split()
for i in range(n):
    sum+=int(s[i])
print(sum)

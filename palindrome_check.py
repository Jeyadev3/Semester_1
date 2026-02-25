N=input("Enter the number:")
rev=""
for i in N:
    rev=i+rev
if N==rev:
    print(N,"is a palindrome")
else:
    print(N,"is not a palindrome")

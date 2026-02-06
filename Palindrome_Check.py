def palindrome(n):
    rev=n[::-1]
    if rev==n:
        return("The given string is a palindrome")
    else:
        return("The given string is not a palindrome")
n=input("Enter the string :")
p=palindrome(n)
print(p)



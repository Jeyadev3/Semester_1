def pangram(n):
    num=n.lower()
    alp="abcdefghijklmnopqrstuvwxyz"
    for i in alp:
        if i not in num:
            return("The given string is not a pangram")
    return("The given string is a pangram")
n=input("Enter the string :")
p=pangram(n)
print(p)

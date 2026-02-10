n=int(input("Enter n :"))
elements=input("Enter elements :")
s=elements.split()
for i in range(len(s)):
    s[i]=int(s[i])
print("Maximum :",max(s))
print("Minimum :",min(s))

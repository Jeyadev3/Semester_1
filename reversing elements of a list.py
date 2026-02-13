n = int(input("Enter n :"))
elements = input("Enter elements :")
s = elements.split()
for i in range(len(s)):
    s[i] = int(s[i])
s.reverse()
print("Reversed list :", s)

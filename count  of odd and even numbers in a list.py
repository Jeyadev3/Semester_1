n = int(input("Enter n : "))
elements = input("Enter elements : ")
s = elements.split()
for i in range(len(s)):
    s[i] = int(s[i])
even = 0
odd = 0
for num in s:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Number of even elements :", even)
print("Number of odd elements  :", odd)

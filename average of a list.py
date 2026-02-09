n = int(input("Enter n: "))
s = input("Enter elements: ").split()
for i in range(len(s)):
    s[i] = int(s[i])
avg = sum(s) / n
print("Average ",avg)

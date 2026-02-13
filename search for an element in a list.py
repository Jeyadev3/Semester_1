n = int(input("Enter n: "))
elements = input("Enter elements: ")
s = elements.split()
for i in range(len(s)):
    s[i] = int(s[i])
item = int(input("Enter element to search: "))
if item in s:
    position = s.index(item) + 1   
    print(item, "found at position", position)
else:
    print(item, "not found in the list")

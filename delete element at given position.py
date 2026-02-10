n = int(input("Enter n: "))
s = input("Enter elements: ").split()
pos = int(input("Enter position to delete: "))
del s[pos - 1]
print("Updated list:", s)

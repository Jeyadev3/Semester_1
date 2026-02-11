n = int(input("Enter n: "))
s = input("Enter elements: ").split()
print("Elements in odd positions:", end=" ")
for i in range(0, n, 2):
    print(s[i], end=" ")

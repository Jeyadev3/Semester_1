largest=0
while True:
    N=int(input("Enter a number :"))
    if N==0:
        break
    elif largest < N:
        largest=N
print("largest number is :",largest)


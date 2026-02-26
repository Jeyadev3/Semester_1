N=int(input("Enter the number :"))
sum=0
for i in range(N):
    M=int(input("Enter the number:"))
    if M%2!=0:
        sum+=M
print("Sum of the odd numbers is:",sum)        

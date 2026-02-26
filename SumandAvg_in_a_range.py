sum=0
avg=0
N=int(input("How many numbers? "))
for i in range(N):
    M=int(input("Enter number :"))
    sum+=M
avg=sum/N
print(avg)

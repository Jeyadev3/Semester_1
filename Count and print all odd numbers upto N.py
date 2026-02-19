count=0
N=int(input("Enter a number :"))
for i in range(1,N+1):
    if i%2!=0:
        count+=1
        print(i,end=" ")
print()
print(count)

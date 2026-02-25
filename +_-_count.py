N=int(input("How many number? "))
positive_count=0
negative_count=0
for i in range(N):
    M=int(input("Enter the number:"))
    if M>0:
        positive_count+=1
    elif M<0:
        negative_count+=1
print("Positive count",positive_count)
print("Negative count",negative_count)

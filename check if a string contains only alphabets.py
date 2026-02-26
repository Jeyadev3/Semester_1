Num=0
N=input("Enter a string :")
for i in N:
    if i.isalpha():
        Num+=1
if Num == len(N):
    print("Contains only Alphabets")
else:
    print("Not only alphabets")
            

sum=0
N=0
n=input("Enter a sring :")
for i in n:
    if i.isdigit():
        sum+=int(i)
        N+=1
print(sum)
avg=sum/N
print(avg)

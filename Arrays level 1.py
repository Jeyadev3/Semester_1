'''Q1.
import array as arr
n=int(input("Entger the total no of elements :"))
A=arr.array('i',[])
for i in range(n):
    m=int(input("Enter the elements :"))
    A.append(m)
sum=sum(A)
print("Total sum is :",sum)'''

'''Q2.
import array as arr
A=arr.array('i',[])
n=int(input("Enter total no of elements :"))
for i in range(n):
    m=int(input("Enter the elements :"))
    A.append(m)
max=A[0]
min=A[0]
for j in A:
    if j>max:
        max=j
    if j<min:
        min=j
print("Largest element is :",max)
print("Smallest element is :",min)'''

'''Q3.    
import array as arr
A=arr.array('i',[])
n=int(input("Enter the total no of elements :"))
for i in range(n):
    m=int(input("Enter the elements :"))
    A.append(m)
odd_count=0
even_count=0
for j in A:
    if j%2==0:
        even_count+=1
    if j%2!=0:
        odd_count+=1
print("Count of odd numbers :",odd_count)
print("Count of even numbers :",even_count)'''

'''Q4.
import array as arr
A=arr.array('i',[])
n=int(input("Enter the total no of elements :"))
for i in range(n):
    m=int(input("Enter the elements :"))
    A.append(m)
l=A[0]
l1=A[0]
for x in A:
    if x>l:
        l=x
    for y in A:
        if y>l1:
            l1=y
product=l*l1
print(product)'''

'''Q5.
import array as arr
A=arr.array('i',[])
n=int(input("Enter the total no of elements :"))
for i in range(n):
    m=int(input("Enter the elements :"))
    A.append(m)
new=arr.array('i',[])
for num in A:
    if num not in new:
        new.append(num)
print(new)'''
    
'''Q6.
import array as arr
A=arr.array('i',[])
n=int(input("Enter the total no of elements :"))
for i in range(n):
    m=int(input("Enter the elements :"))
    A.append(m)
z=arr.array('i',[])
for j in range(len(A)-1,-1,-1):
    z.append(A[j])
print(z)'''

'''Q7.
import array as arr
temp=arr.array('i',[])
n=int(input("Enter the no of days :"))
for i in range(n):
    m=int(input("Enter the temperature :"))
    temp.append(m)
count=0
sum=sum(temp)
avg=sum/n
print("Average temperature is :",avg)
for i in range(n):
    if temp[i]>avg:
        count+=1
print("No of days temperature  was above average is :",count)'''

'''Q8.
import array as arr
A=arr.array('i',[])
n=int(input("Enter the total no of days :"))
for i in range(n):
    m=int(input("Enter the sales figure :"))
    A.append(m)
s=sum(A)
print(s)
maxi=max(A)
pro = []
print(A.index(max(A))+1)
for i in range(0,len(A)-1):
    if A[i] == len(A)+1:
        break
    else:
        pr_per = (A[i+1]-A[i])/A[i]
        pro.append(pr_per)
print(pro)'''

'''Q9.
import array as arr
readings=input("Enter sensor readings: ").split()
a = arr.array('f', [])
for x in readings:
    a.append(float(x))

LOW = 0
HIGH = 100
for i in range(len(a)):
    if a[i] < LOW or a[i] > HIGH:
        if i == 0:                     
            a[i] = a[i + 1]
        elif i == len(a) - 1:           
            a[i] = a[i - 1]
        else:                           
            a[i] = (a[i - 1] + a[i + 1]) / 2

print("Filtered readings:", end=" ")
for x in a:
    print(x, end=" ")'''

'''Q10.
import array as arr
orders_input=input("Enter ordered product IDs: ").split()
orders=arr.array('i', [])
for x in orders_input:
    orders.append(int(x))
stock_input = input("Enter product IDs in stock: ").split()
stock=arr.array('i', [])
for x in stock_input:
    stock.append(int(x))
fulfillable=arr.array('i', [])
out_of_stock=arr.array('i', [])
for item in orders:
    if item in stock:
        fulfillable.append(item)
    else:
        out_of_stock.append(item)
print("Fulfillable orders:", end=" ")
for x in fulfillable:
    print(x, end=" ")
print()
print("Out of stock products:", end=" ")
for x in out_of_stock:
    print(x, end=" ")'''





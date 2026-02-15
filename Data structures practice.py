'''Q1.
l1=[]
l=[]
s=set()
n=int(input("Enter the total no of elements in list :"))
for i in range(n):
    num=int(input("Enter the element :"))
    l.append(num)
n1=int(input("Enter the total no of elements in set :"))
for j in range(n1):
    nu=int(input("Enter the element :"))
    s.add(nu)
print(l)
print(s)
for i in l:
    if i in s:
        l1.append(i)
print(l1)'''

'''Q2.
ans=[]
std=[]
ans_key=input("Enter the answer key :")
ans.append(ans_key)
n=int(input("Enter the total no of students :"))
for i in range(n):
    std_ans=input("Enter the answer marked by student :")
    std.append(std_ans)
mark=[]
for student in std:
    m=0
    for i in range(len(ans_key)):
        if student[i]==ans_key[i]:
            m+=1
    mark.append(m)
print(mark)'''




    



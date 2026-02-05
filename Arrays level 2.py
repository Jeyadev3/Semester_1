'''Q1.
import array as arr
values = input("Enter elements: ").split()
A = arr.array('i', [])
for v in values:
    A.append(int(v))
result = arr.array('i', [-1] * len(A))
for x in A:
    if x != -1 and x < len(A):
        result[x] = x
print("Rearranged array:", end=" ")
for x in result:
    print(x, end=" ")'''

'''Q2.
import array as arr
values = input("Enter elements: ").split()
A = arr.array('i', [])
for v in values:
    A.append(int(v))
for i in range(1, len(A)):
    if i % 2 == 0:
        if A[i] < A[i - 1]:
            A[i], A[i - 1] = A[i - 1], A[i]
    else:
        if A[i] > A[i - 1]:
            A[i], A[i - 1] = A[i - 1], A[i]
print("Rearranged array:", end=" ")
for x in A:
    print(x, end=" ")'''

'''Q3.
import array as arr
values = input("Enter elements: ").split()
A = arr.array('i', [])
for v in values:
    A.append(int(v))
pos = 0
for i in range(len(A)):
    if A[i] != 0:
        A[pos] = A[i]
        pos += 1
while pos < len(A):
    A[pos] = 0
    pos += 1
print("Updated array:", end=" ")
for x in A:
    print(x, end=" ")'''

'''Q4.
import array as arr
values = input("Enter elements: ").split()
A = arr.array('i', [])
for v in values:
    A.append(int(v))
x = int(input("Enter sum value: "))
found = False
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] + A[j] == x:
            print(A[i], ",", A[j])
            print("Valid pair exists.")
            found = True
            break
    if found:
        break
if not found:
    print("No valid pair exists.")'''


'''Q5.
import array as arr
values = input("Enter elements: ").split()
A = arr.array('i', [])
for v in values:
    A.append(int(v))
pos = 0
for i in range(len(A)):
    if A[i] != 0:
        A[pos] = A[i]
        pos += 1
while pos < len(A):
    A[pos] = 0
    pos += 1
print("Updated array:", end=" ")
for x in A:
    print(x, end=" ")'''

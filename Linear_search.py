def search(list,num):
    for i in range(len(list)):
        if list[i]==num:
            return i+1
    return -1


list=[1,3,5,7,9]
num=5
pos = search(list,num)
if pos == -1:
    print("Not Found")
else:
    print("Found at ",pos)

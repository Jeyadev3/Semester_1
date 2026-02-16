def bubblesort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
            

list=[1,5,2,6,8,4]
print(bubblesort(list))

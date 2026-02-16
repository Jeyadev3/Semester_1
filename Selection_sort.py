def selection_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                arr[j],arr[i]=arr[i],arr[j]
    return arr
                


arr=[8,2,4,1,6,5,6]
print(selection_sort(arr))

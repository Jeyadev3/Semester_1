pos=-1
def search(list,num):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==num:
            globals()['pos']=mid+1
            return True
        else:
            if list[mid]>num:
                u=mid-1
            else:
                l=mid+1
    return False
        
            
list=[1,3,5,7,9,11,13,15,17,19,21,23]
num=3
if search(list,num):
    print("Found at ",pos)
else:
    print("Not Found")

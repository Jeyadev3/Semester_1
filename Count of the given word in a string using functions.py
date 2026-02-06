def count(words):
    w=words.split()
    count={}
    for i in w:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count
words=input("Enter the string :")
c=count(words)
print(c)

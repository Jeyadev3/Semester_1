def Add_student(name):
    if name not in record:
        record[name]=[]
        print("Student added")
    else:
        print("Student already exists")

def Add_marks(name,l):
    record[name].extend(l)
    print(record)

def average_marks(name):
    m=sum(record[name])/len(record[name])
    print(m)

def grade_student(name):
    for m in record[name]:
        if m>=90:
            grade="O"
        elif m>=80:
            grade="A"
        elif m>=70:
            grade="B"
        elif m>=60:
            grade="C"
        elif m>=50:
            grade="P"
        else:
            grade="F"
        print(m," , ",grade)
    
record={}

while True:
    print("\n1. Add student")
    print("2. Add marks")
    print("3. Calculate average")
    print("4. Assign grades")
    print("5. Exit")
    
    choice=int(input("Enter the choice :"))

    if choice==1:
        name=input("Enter the name of the student :")
        Add_student(name)

    elif choice==2:
        l=[]
        name=input("Enter the name :")
        n=int(input("Enter the no of marks to be added :"))
        for i in range(n):
            marks=int(input("Enter the marks :"))
            l.append(marks)
        Add_marks(name,l)

    elif choice==3:
        name=input("Enter the name :")
        average_marks(name)

    elif choice==4:
        name=input("Enter the name :")
        grade_student(name)

    elif choice==5:
        break

    else:
        print("Invalid choice")
    


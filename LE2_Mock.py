def add_student(name_list,students_list,status_dict):
    name=input("Enter the name :")
    year=input("Enter the year :")
    name_list.append(name)
    students_list.append((name,year))
    status_dict[name]="Active"
    print("Done successfully")

def update_activities(s,new):
    if new not in s:
        s.add(new)
    else:
        print("Already present")
    print("Updated activities ",s)

def check_membership(status_dict,name_list,n):
    if n not in name_list:
        print("Record not found")
    else:
        print(status_dict[n])
    count=0
    for i,j in status_dict.items():
        if j=="Active":
            count+=1
    print(count)

def display(name_list,students_list,status_dict,s):
    print(name_list)
    print(students_list)
    print(status_dict)
    print(s)

name_list=[]
students_list=[]
status_dict={}
s=set()

while True:
    print("\n------Menu-------")
    print("1. Add student")
    print("2. Add activity")
    print("3. Check membership")
    print("4. Display all data")
    print("5. Exit")

    choice=int(input("Enter the choice :"))

    if choice==1:
        add_student(name_list,students_list,status_dict)

    elif choice==2:
        new=input("Enter the new string :")
        update_activities(s,new)

    elif choice==3:
        n=input("Enter name to check :")
        check_membership(status_dict,name_list,n)

    elif choice==4:
        display(name_list,students_list,status_dict,s)

    elif choice==5:
        break

    else:
        print("Invalid choice")
        
        

def Add_contact(name,number):
    phonebook[name]=number
    print("Contact added")

def Search_contact(name):
    if name in phonebook:
        print(name,":",phonebook[name])
    else:
        print("Contact not found")

def Delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted")
    else:
        print("Contact not found")

def display():
    if len(phonebook)!=0:
        for i,j in phonebook.items():
            print(i,":",j)
    else:
        print("Phonebook is empty")

phonebook={}
while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit")

    choice=int(input("Enter choice :"))

    if choice==1:
        name=input("Enter the name :")
        number=int(input("Enter the number :"))
        Add_contact(name,number)

    elif choice==2:
        name=input("Enter name to search :")
        Search_contact(name)

    elif choice==3:
        name=input("Enter name to delete :")
        Delete_contact(name)

    elif choice==4:
        display()

    elif choice==5:
        break

    else:
        print("Invalid choice")

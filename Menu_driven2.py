def avg_temp(data):
    sum=0
    for i in data:
        sum+=i["temp"]
        avg=sum/len(data)
    print("The average temperature is :",avg)

def most_rain(data):
    max=data[0]["rain"]
    day=data[0]["date"]
    for i in data:
        if i["rain"]>max:
            max=i["rain"]
            day=i["date"]
    print("The day with most rain is ",day," with ",max)

def threshold_temp(t,data):
    day=[]
    for i in data:
        if i["temp"]>t:
            day.append(i["date"])
    print("All days above a temperature threshold is ",day)
            

data=[]
n=int(input("Enter no of days :"))
for i in range(n):
    date=input("Enter the date :")
    temp=int(input("Enter the temperatue :"))
    rain=int(input("Enter rainfall :"))
    data.append({"date":date,"temp":temp,"rain":rain})
print(data)

while True:
    print("\n1. Average temperature")
    print("2. Day with most rain")
    print("3. All days above threshold temperature")
    print("4. Exit")

    choice=int(input("Enter the choice :"))

    if choice==1:
        avg_temp(data)

    elif choice==2:
        most_rain(data)

    elif choice==3:
        t=int(input("Enter threshold temperature :"))
        threshold_temp(t,data)

    elif choice==4:
        break

    else:
        print("Invalid choice")

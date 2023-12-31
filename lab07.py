import random
orderDetails={"order":[]}

def Orderid():
    rand=[0]*5
    for i in range(0,5):
        rand[i]=str(random.randint(0,9))
    return rand[0]+rand[1]+rand[2]+rand[3]+rand[4]

def create():
    print("Menu")
    print("*"*30)
    print("Item   Price")
    newOrder={"orderID":None,"items":[]}
    newOrder["orderID"]=Orderid()
    while True:
        j=0
        for i in priceList:
            j+=1
            print(j,i[0],i[1])
        itemno=int(input("Enter required item number (0 to stop order): "))
        if itemno in range(1,7):
            item={"itemnumber":None,"quantity":None}
            quantity=int(input("Enter the required quantity: "))
            item["itemnumber"]=itemno
            item["quantity"]=quantity
            newOrder["items"].append(item)
        elif itemno==0:
            print("Thank you for your order")
            orderDetails["order"].append(newOrder)
            break
        else:
            print("Please enter the correct item number")

def viewOrder():
    sum=0
    for i in range(0,len(orderDetails["order"])):
        print("Order ID:",orderDetails["order"][i]["orderID"])
        print("Item   Quanity   Amount")
        for j in range(0,len(orderDetails["order"][i]["items"])):
            amount=int(orderDetails["order"][i]["items"][j]["quantity"])*int(priceList[int(orderDetails["order"][i]["items"][j]["itemnumber"])-1][1])
            print(priceList[int(orderDetails["order"][i]["items"][j]["itemnumber"])-1][0],"  ",orderDetails["order"][i]["items"][j]["quantity"],"     ",amount)
            sum=sum+amount
    print("Your total bill amount is ",sum)

priceList=[["dish1",20],["dish2",40],["dish3",55],["dish4",70],["dish5",35],["dish6",45]]
print("*"*30)
print("Welcome to The Restocafe")
print("*"*30)
while True:
    print("\nSelect your action based on these requirements")
    print("1. Create new order\n2. View Orders\n3. Exit")
    choice=int(input("Your requirement:"))
    if choice==1:
        create()
        print(orderDetails)
    elif choice==2:
        viewOrder()
    elif choice==3:
        exit()
#Create an inventory system tracking items and quantities with a dictionary
n=int(input("Enter the number of items to be added in the inventory: "))
stocks={}
for i in range(n):
    item=input("Enter the item to be added in the inventory: ")
    quantity=int(input("Enter the quantity of the items: "))
    stocks[item]=quantity
#Print the inventory3
print("----------The available stocks in the inventory are:------- ")
for key,value in stocks.items():
    print(key,"-",value)   
print("------------------------------------------------------------")    

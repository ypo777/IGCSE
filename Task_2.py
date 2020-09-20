#Showing Items to Customer
customizedComputer = {"Case": 0.0,"RAM": 0.0,"Main Hard Disk Drive": 0.0}
def showingItemsWithData(caseCode):
    print("Code" + " Descritpion " + "\t Price")
    for x in caseCode:
        itemData = {}
        itemData["Code"]  = x
        itemData["Price"]  =  itemCodeAndPrice_Array.get(x)
        itemData["Descritpion"] = itemCodeAndDescription_array.get(x)
        print(itemData.get("Code") ,"\t", itemData.get("Descritpion"),"\t\t", itemData.get("Price"))

def showingItemsAndChooseingItems(array_one):
    for c in array_one:
        if c == "Case":
            print("Case with Type and Price ")
            print("------------------------")
            showingItemsWithData(category_array.get(c))
            choosenItem(customizedComputer,c)
        if c == "RAM":
            print("RAM with Type and Price ")
            print("------------------------")
            showingItemsWithData(category_array.get(c))
            choosenItem(customizedComputer,c)
        if c == "Main Hard Disk Drive":
            print("Main Hard Disk Drive with Type and Price ")
            print("------------------------")
            showingItemsWithData(category_array.get(c))
            choosenItem(customizedComputer,c)
    moreItems = input("Do you want to choose additional items? (Y or N) \n")
    if moreItems == "Y":
      for c in array_one:
        if c == "Solid State Drive":
            print("Solid State Drive with Type and Price ")
            print("------------------------")
            showingItemsWithData(category_array.get(c))
            choosenItem(customizedComputer, c)
        if c == "Second Hard Disk Drive":
            print("Second Hard Disk Drive with Type and Price ")
            print("------------------------")
            showingItemsWithData(category_array.get(c))
            choosenItem(customizedComputer, c)
        if c == "Optical Drive":
            print("Optical with Type and Price ")
            print("------------------------")
            showingItemsWithData(category_array.get(c))
            choosenItem(customizedComputer, c)
        if c == "Operating System":
            print("Operating System with Type and Price ")
            print("------------------------")
            showingItemsWithData(category_array.get(c))
            choosenItem(customizedComputer, c)

def outputResult():
    totalPrice = 0.0
    for value in customizedComputer.values():
        totalPrice = totalPrice + value
    totalPrice = "{:.2f}".format(totalPrice)
    print("---------------------")
    print("Total Cost of Your Computer")
    for key, value in customizedComputer.items():
        print(str(key) + ":" + str(value))
    print("---------------------")
    print("Total Price " + ":" + str(totalPrice))

def choosenItem (array_list,indexPC):
    choosedItemCode = input("Enter Item Code : ")
    array_list[indexPC] = itemCodeAndPrice_Array.get(choosedItemCode)


# Data Arrays of Program
category_array  =       {"Case":('A1','A2'),
                         "RAM":('B1','B2','B3'),
                         "Main Hard Disk Drive":('C1','C2','C3'),
                         "Solid State Drive":('D1','D2'),
                         "Second Hard Disk Drive":('E1','E2','E3'),
                         "Optical Drive":('F1','F2'),
                         "Operating System":('G1','G2')}
itemCodeAndPrice_Array =       {'A1': 75.00,'A2':150.00,
                       'B1': 79.99,'B2':149.99,'B3':299.99,
                       'C1':49.99,'C2':89.99,'C3':129.99,
                       'D1':59.99,'D2':119.99,
                       'E1':49.99,'E2':89.99,'E3':129.99,
                       'F1':50.00,'F2':100.00,
                       'G1':100.00,'G2':175.00}
itemCodeAndDescription_array =     {"A1":'Compact',"A2":'Tower',
                          "B1":'8GB',"B2":'16GB',"B3":'32GB',
                          "C1":'1TB HDD',"C2":'2TB HDD',"C3":'4TB HDD',
                          "D1":'240GB SSD',"D2":'480GB SSD',
                          "E1":'1TB HDD',"E2":'2TB HDD',"E3":'4TB HDD',
                          "F1":'DVD/Blu-Ray Player',"F2":'DVD/Blu-Ray Re-writer',
                          "G1":'Standard Version',"G2":'Professional Version'}

#Calling Functions
showingItemsAndChooseingItems(category_array)
outputResult()



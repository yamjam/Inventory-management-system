def shop():
    r=0
    a=[[1,"Mango",12,50,"Fruits"],
       [2,"Samsung GalaxyS8",800,10,"Electronics"],
       [3,"Wheat Tortilla",3,100,"Whole Food"],
       [4,"Toothpaste",4,500,"Personal Care"],
       [5,"Facewash",15,100,"Personal Care"],
       [6,"Make up",18,40,"Beauty Product"],
       [7,"Basmati Rice",8,100,"Whole Food"],
       [8,"Apple",2,30,"Fruit"],
       [9,"Toothbrush",10,100,"Personal Care"],
       [10,"Pringles",4,100,"Snacks"],
       [11,"Wavy Lays",2,200,"Snacks"]]
    #While loop is used so that the program runs infinite times until the user wants to kill it
    while r==0:
        def menu():
            print("Press 1 to list down all the items in store")
            print("Press 2 to add a new item in store")
            print("Press 3 to update an existing item in store")
            print("Press 4 to delete an item from the store")
            print("Press 5 to check out an item from the store")
            print("Press 6 to check in an item in the store")
            print("Press 7 to exit")
        menu()
        num= int(input())

        if num==1:
            def list1():
                print("-"*61)
                print(": Item id : Name"," "*5," : Price  : Count  : Category"," "*6,":")#Table is made based on sum calculations
                print("-"*61)
                for item in a:
                    print(":",item[0]," "*(6-len((str(item[0])))),":",
                          item[1]," "*(10-len(item[1])),":",
                          item[2]," "*(5-len(str(item[2]))),":",
                          item[3]," "*(5-len(str(item[3]))),":",
                          item[4]," "*(14-len(item[4])),":")
                    print("-"*61)
            list1()

        if num==2:
            def new():
                s=int(input("Enter the serial number of the product "))
                n=str(input("Enter the name of the product "))
                p=int(input("Enter the price of the product "))
                q=int(input("What is the quantity of the product? "))
                cat=str(input("What is the category of the product "))
                b=[s,n,p,q,cat]
                a.append(b)
                return()
            new()

        if num==3:
            def update():
                print("-"*61)
                print(": Item id : Name"," "*5," : Price  : Count  : Category"," "*6,":")#Table is made based on sum calculations
                print("-"*61)
                for item in a:
                    print(":",item[0]," "*(6-len((str(item[0])))),":",
                          item[1]," "*(10-len(item[1])),":",
                          item[2]," "*(5-len(str(item[2]))),":",
                          item[3]," "*(5-len(str(item[3]))),":",
                          item[4]," "*(14-len(item[4])),":")
                    print("-"*61)
                e=0
                while e==0:
                    x=int(input("Which product do you want to update? Enter the item id"))
                    for i in range(0,len(a)):
                        if x in a[i]: #This condition access every sublist and find the match in them
                            l=int(input("Choose what you want to change:\n 1) Item id\n 2) Name\n 3) Price\n 4) Category "))
                            if l==1:
                                s=int(input("Update the serial number of the product "))
                                a[i][0]=s
                            if l==2:
                                n=str(input("Update the name of the product "))
                                a[i][1]=n
                            if l==3:
                                p=int(input("Update the price of the product "))
                                a[i][2]= p
                            if l==4:
                                cat=str(input("Update the category of the product "))
                                a[i][4]=cat
                        else:
                            continue
                    k=str(input("Do you want to update another item? Yes or No? "))
                    if k== "Yes":
                        continue
                    elif k=="No":
                        break
                    return()
            update()

        if num==4:
            def delete():
                e= 0
                while e==0:
                    x=int(input("Which product do you want to Delete? Enter the item id "))
                    for i in range(0,len(a)):
                        if x in a[i]:
                            del a[i]
                            print("The requested product has been deleted")
                            break
                        else:
                            continue
                    k=str(input("Do you want to delete another product? Yes or No? "))
                    if k== "Yes":
                        continue
                    elif k=="No":
                        break
                return()
            delete()

        if num==5:
            def out():
                e=0
                while e==0:
                    x=int(input("Which product was bought? Enter the item id "))
                    for i in range(0,len(a)):
                        if x in a[i]:
                            g= a[i][3] #Takes the value of particular key for futhur calculation
                            u=int(input("Enter the quantity of the product "))
                            j= g-u #decreases the value of count
                            a[i][3]= j #replaces the value of count with new one
                            break
                        else:
                            continue
                    k=str(input("Do you want to buy another item? Yes or No? "))
                    if k== "Yes":
                        continue
                    elif k=="No":
                        break
                return()
            out()

        if num==6:
            def add():
                e=0
                while e==0:
                    x=int(input("Which product do you want to add? Enter the item id "))
                    for i in range(0,len(a)):
                        if x in a[i]:
                            g= a[i][3]#Takes the value of particular key for futhur calculation
                            u=int(input("Enter the quantity of product "))
                            j= g+u #increases the count of the product
                            a[i][3]= j #replaces the value of count with new one
                            break
                        else:
                            continue
                    k=str(input("Do you want to add another item? Yes or No? "))
                    if k== "Yes":
                        continue
                    elif k=="No":
                        break
                return()
            add()

        if num==7:
            break
shop()
    
            
            
    
        




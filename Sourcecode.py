correct=True 
while correct : 
    name = input("Enter Username: ")
    if name == 'Admin'.lower(): 
        pw = input("Enter passcode: ")
        if pw == 'test':
            print('Access granted')


            import json
            
            def menu():
                print(' '*20,'Cloth Store ', ' '*20) 
                print('-'*50)
                print(' '*15, ' M e n u  O p t i o n s ',' '*15)
                print('-'*50) 
                print(' '*14,'C L A S S I C   W E A R ') 
                print('-'*50) 
                print('1)  New Stock Entry') 
                print('2)  Modify Information') 
                print('3)  Delete Item  ') 
                print('4)  Stock List (Display all)')
                print('5)  Search by Category') 
                print('6)  Search by Brand Name') 
                print('7)  Search by Size') 
                print('8)  Search by Color') 
                print('9)  Search by Price')
                print('10) EXIT') 
                print('-'*50) 

            def line():
                print('-'*50) 

            def initial():
                d[1]=['Polo','Burberry', 'Large', 'Navy', 13500,] 
                d[2]=['Sweatshirt','Balenciaga', 'Medium','Grey', 22800]
                d[3]=['Trackpants','Prada', '42', 'Olive', 8450] 
                d[4]=['Hoodie','Dior', 'Extra Small', 'Ash Grey', 13250]
                d[5]=['Jacket','Raph Lauren', 'Extra Large', 'Midnight Black', 9150] 

                count=6

            def nentry(count):
                #clothid=int(input('Enter Book id')) 
                clothid=count
                print('Cloth ID   : ', clothid)
                catag=input('Enter Category: ')
                bname=input('Enter Brand Name: ')
                size=input('Enter Size: ')
                color=input('Enter Color: ')
                price=float(input('Enter Price: '))
                rec=[catag,bname,size,color,price]
                d[clothid]=rec

            def modifyinfo():
                ubid=int(input('Enter Cloth ID: '))
                rec=list(d.get(ubid,"Not Found"))
                print(rec)
                print(type(rec))
                if rec=="Not Found":
                     print('Record Does not Exist')
                else:
                    print(rec)
                    ucat=rec[0]
                    ubname=rec[1]
                    usize=rec[2]
                    ucolor=rec[3]
                    uprice=rec[4]
                    print("What would you like to change?\n1)Category\n2)Brand Name\n3)Size\n4)Color\n5)Price\n6)All")
                    option=int(input("Enter Option 1/2/3/4/5/6: "))
                    if option==1:
                        rec[0]=input("Enter Category: ")
                    elif option==2:
                        rec[1]=input("Enter Brand Name: ")
                    elif option==3:
                        rec[2]=input('Enter Size: ')
                    elif option==4:
                        rec[3]=input('Enter Color: ')
                    elif option==5:
                        rec[4]=int(input('Enter Price: '))
                    elif option==6:
                        rec[0]=input("Enter Category: ")
                        rec[1]=input("Enter Brand Name: ")
                        rec[2]=input('Enter Size: ')
                        rec[3]=input('Enter Color: ')
                        rec[4]=int(input('Enter Price: '))
                    d[ubid]=rec

            def deleteinfo():
                ubid=int(input("Enter Cloth ID: "))
                rec=list(d.get(ubid,"Notfound"))
                if rec==("Not Found"):
                    print("Record Does not Exist")
                else:
                    print(d.pop(ubid), "\nitem successfully removed")

            def dispall():
                print('Cloth Records')
                line()
                for k in d:
                    print('Category: ',d[k][0])
                    print('Brand Name: ',d[k][1])
                    print('Size: ',d[k][2])
                    print('Color: ',d[k][3])
                    print('Price: ',d[k][4])
                    print('-'*20)


            def searchbycategory():
                print('-'*50)
                print('Search Category')
                print(' ')
                ucate=input('Enter Category to be Searched: ')
                for k in d:
                    if d[k][0].lower()== ucate.lower():
                        print('-'*50)
                        print('Category: ',d[k][0])
                        print('Brand Name: ',d[k][1])
                        print('Size: ',d[k][2])
                        print('Color: ',d[k][3])
                        print('Price: ',d[k][4])

            def searchbyname():
                print('-'*50)
                print('Search Brand Name')
                ubname=input('Enter Brand name to be Searched: ')
                for k in d:
                    if d[k] [1].lower() ==ubname.lower():
                        print('-'*50)
                        print('Brand Name : ',d[k][1])
                        print('Category: ',d[k][0])
                        print('Size : ',d[k][2])
                        print('Color: ',d[k][3])
                        print('Price: ',d[k][4])

            def searchbysize():
                print('-'*50)
                print("Search by Size")
                usize=input("Enter Size: ")
                for k in d:
                    if d[k] [2].lower()==usize.lower():
                        print('-'*50)
                        print('Size: ',d[k][2])
                        print('Category: ',d[k][0])
                        print('Brand Name: ',d[k][1])
                        print("Color: ", d[k][3])
                        print("Price: ",d[k][4])

            def searchbycolor():
                print("Search By Color")
                ucolor=input('Enter Color: ')
                for k in d:
                    if d[k] [3].lower()==ucolor.lower():
                        print('-'*50)
                        print('Color: ',d[k][3])
                        print('Category: ',d[k][0])
                        print('Brand Name: ',d[k][1])
                        print('Size: ',d[k][2])
                        print('Price', d[k][4])

                    else:
                        print('Record Does not exist')

            def searchbyprice(): 
                print("Search By Price")
                uprice=float(input("Enter Price: "))
                for k in d:
                    if d[k][4]==uprice:
                        print('-'*50)
                        print('Price : ',d[k][4])
                        print('Category: ',d[k][0])
                        print('Brand Name : ',d[k][1])
                        print('Size : ',d[k][2])
                        print('Color : ',d[k][3])
                    else:
                        print('Record Does not exist')



            #Main function
            count=6
            d={}
            #rec=[ucat,bname,size,color,Price]
            initial()
            ch='y'
            while True:
                menu()
                option=int(input("Enter Option: "))
                if option==1:
                    nentry(count)
                    count=count+1
                if option==2:
                    modifyinfo()
                if option==3:
                    deleteinfo()
                if option==4:
                    dispall()
                if option==5:
                    searchbycategory()
                if option==6:
                    searchbyname()
                if option==7:
                    searchbysize()
                if option==8:
                    searchbycolor()
                if option==9:
                    searchbyprice()
                else:
                    print('-'*50)
                    print(' ')
                    print(' Learn new things everyday. Enjoy each day to the fullest and make memories for life. Have a great day. ')
                    print(' ')
                    print(' ')
                    ch=input('Do you wish to continue(y/n): ')
                    if ch == 'n':
                        break
                    else:
                        continue   
                
                break






        if pw != "test":
            pwi=input('password incorrect,would you like to try the username and passcode again? y/n: ')
            if pwi =='y'.lower():
                correct=True

            else:
                print('Thanks for login. Have a wonderfull day ahead! ^_^  ')
                quit()

          
          

    if name !="Admin".lower():
        uni = input("username incorrect , would you like to try the username again y/n? ")
        if uni == "y".lower():
          correct = True 
        else:
         print("Thanks for login. Have a wonderful day ahead! ^_^  ")
         quit()

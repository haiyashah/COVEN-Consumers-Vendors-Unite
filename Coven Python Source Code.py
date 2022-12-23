#Imports
import mysql.connector
from time import sleep
from PIL import Image

#Python-SQL Connection
mydb = mysql.connector.connect(
host="localhost",
   	port=3306,
   	user="root",
  	 password="r00ting@you2",
   	database="coven",
)
mycursor = mydb.cursor()

#User-defined Functions
###Separator
def dash():
   	dash = '-'*25
   	for i in range(25):
       		print(dash[i], sep='', end='', flush=True); sleep(0.08)
   	print()

###Consumer Details
def cons_det():
   	cname = input("Enter your name:")
   	car = input("Enter your address:")
   	cphone = input("Enter your phone number:")
   	cprod=input("Enter the product you want to buy:")
  	 mycursor = mydb.cursor()
   	sql = "INSERT INTO Consumer_Table (Consumer_Name, Area, 
                        Consumer_Phone_No, Product) VALUES (%s, %s,%s,%s)"
   	val = (cname, car, cphone, cprod)
   	mycursor.execute(sql, val)
   	mydb.commit()

###Consumer choice filter-1 ; (Sp Prod, Any Ar)
def cons_ch_14():
   	print("Selected option: Specific product, Any area")
   	sp_prod=input("Enter the required product:")
   	dash()
   	mycursor = mydb.cursor()
	sql = "SELECT Vendor_Name,Product,Rate,Area,Timings FROM Vendor_Table  
                        WHERE Product =%s"

        mycursor.execute(sql,(sp_prod,))
   	myresult = mycursor.fetchall()
   	if (not myresult):
       		print("No Matches Found!")
   	else:
       		for x in myresult:
          			 print("Your search results are:")
           			print("Vendor Name, Product, Rate, Area, Timing")
           			print(x)

###Consumer choice filter-2 ; (Sp AR, any prod)
def cons_ch_32():
   	print("Selected option: Specific area, Any product")
   	sp_area=input("Enter the required area:")
   	mycursor = mydb.cursor()
   	sql = "SELECT Vendor_Name,Product,Rate,Area,Timings FROM Vendor_Table 
                        WHERE Area =%s"
   	mycursor.execute(sql,(sp_area,))
   	myresult = mycursor.fetchall()
   	if (not myresult):
       		print("No Matches Found!")
   	else:
       		for x in myresult:
          			print("Vendor Name, Product, Rate, Area, Timing")
           			print(x)

###Consumer choice filter-3
def cons_ch_24():
print("Selected option: All products, All areas")
   	print("Vendor Name, Product, Rate, Area, Timing")
   	mycursor = mydb.cursor()
   	sql = "SELECT Vendor_Name,Product,Rate,Area,Timings FROM Vendor_Table"
   	mycursor.execute(sql)
   	myresult = mycursor.fetchall()
   	for x in myresult:
       		print(x)


###Vendor Details
def vend_det():
   	print("Enter your details:")
   	vname = input("Enter your name:")
   	vphone = input("Enter your phone number:")
   	vprod = input("Enter the product you're selling:")
   	vrate = int(input("Enter the rate of your product:"))
   	varea = input("Enter the area where your product is being sold:")

   	vtime = input("Enter the time wherein the specified product is being sold at that area:")
   
  	mycursor = mydb.cursor()
   	sql = "INSERT INTO Vendor_Table (Vendor_Name,Vendor_Phone_No, Product,Rate,Area,Timings) VALUES (%s, %s,%s,%s, %s,%s)"
   	val = (vname, vphone, vprod, vrate, varea, vtime)
   	mycursor.execute(sql, val)
   	mydb.commit()


###Vendor choice filter-1 ; (Sp prod, Any ar)
def vend_ch_14():
   	print("Selected option: Specific product, Any area")
   	sp_prod=input("Enter the required product:")
   	mycursor = mydb.cursor()
   	sql = "SELECT Product,Area FROM Consumer_Table WHERE product =%s"
   	mycursor.execute(sql,(sp_prod,))
   	myresult = mycursor.fetchall()
   	if (not myresult):
       		print("No matches found!")
   	else:
       		print("('Product'),(' Area')")
       		for x in myresult:
           			print(x)


###Vendor choice filter-2 ; (Sp ar, any prod)
def vend_ch_32():
   	print("Selected option: Specific area, Any product")
   	sp_area=input("Enter the required area:")
   	mycursor = mydb.cursor()
   	sql = "SELECT Product,Area FROM Consumer_Table WHERE Area =%s"
   	mycursor.execute(sql,(sp_area,))
  	myresult = mycursor.fetchall()
   	if (not myresult):
       		print("No matches found!")
   	else:
       		print("('Product'),(' Area')")
       		for x in myresult:
           			print(x)



###Vendor choice filter-3
def vend_ch_24():
   	print("Selected option: All products, All areas")
   	   	mycursor = mydb.cursor()
   	sql = "SELECT Product,Area FROM Consumer_Table"
   	mycursor.execute(sql)
   	print("('Product'),(' Area')")
   	myresult = mycursor.fetchall()
   	for x in myresult:
       		print(x)

def coven():
   	print("Welcome to Coven!")
   	print("Where Customers and Producers Unite!")
   	dash()
   	choice=input("Are you a Consumer or Vendor?C/V")
   	dash()

   	if choice=="C" or choice=="c":
       		print("Enter your details below to register yourself")
       		cons_det()
       		print("You have been added!")
       		dash()

       		print("To start buying, select any of the below option(s) by which your 
                                    search will be filtered:")
       		print("1. Specific Product")
       		print("2. All products")
       		print("3. Specific Area")
       		print("4. All Areas")
       		cons_choice=int(input("Enter your choice:"))
       		if cons_choice==1 or cons_choice==14 or cons_choice==41:
           			cons_ch_14()

       		elif cons_choice==3 or cons_choice==32 or cons_choice==23 :
          			 cons_ch_32()

       		elif cons_choice==13 or cons_choice==31:
           		       print("Sorry! Search option unavailable")

       		elif cons_choice==24 or cons_choice==42:
          			cons_ch_24()
       		else:
           			print("Invalid input")
                                dash()

   
                elif choice=="V" or choice=="v":
       		vend_det()

       		print("You have been added!")
       		dash()

       		print("To start selling, select any of the below option(s) by which your 
                                    search will be filtered:")
       		print("1. Specific Product")
       		print("2. All products")
      		print("3. Specific Area")
      		print("4. All Areas")

       		vend_choice=int(input("Enter your choice:"))
       		if vend_choice==1 or vend_choice==14 or vend_choice==41:
           			vend_ch_14()

   		 elif vend_choice==3 or vend_choice==32 or vend_choice==23 :
           			vend_ch_32()

       		elif vend_choice==13 or vend_choice==31:
           			print("Sorry! Search option unavailable")

       		elif vend_choice==24 or vend_choice==42:
           			vend_ch_24()
       		else:
           			print("Invalid input")
       		dash()

                else:
       		print("Invalid input!")

def about():
   	print("About our project:")
   	dash()
   	file = open('farmers_coven.txt', 'r')
   	for each in file:
       		print(each)
       		sleep(1)
   	dash()

   	print("Statistics of our project are:")
   	mycursor = mydb.cursor()
   	sql = "SELECT * FROM Profit_Table"
   	mycursor.execute(sql)
   	myresult = mycursor.fetchall()
   	print("('Product', 'Amount sold before this initiative', 'Amount sold after this 
                       initiative', 'Profit Percentage')")
   	for x in myresult:
       		print(x)
   	dash()

   	print("Graphical representation of how our project made an impact")
   	import matplotlib.pyplot as plt
   	# Crop
   	left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   	# heights of bars
   	height = [8, 12, 25, 100, 30, 60, 18, 24, 25, 50]
   	# labels for bars
   	tick_label = ['Potato before', 'Potato after', 'Apple before', 'Apple after', 'Maize 
                                      before', 'Maize after','Cabbage before', 'Cabbage after', 'Wheat 
                                      before', 'Wheat after']
   	
        # plotting a bar chart
   	plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green'])
   	# naming the x-axis
   	plt.xlabel('Crop')
   	# naming the y-axis
   	plt.ylabel('Rate')
   	# plot title
   	plt.title('Comparing the rates of crop before and after to show the profit')
   	# function to show the plot
   	plt.show()
   	dash()

   	print("This has resulted in both happy consumers and vendors!")
   	img1 = Image.open("vendor.jpg")
   	img1.show()
   	img2 = Image.open("buyer.jpg")
   	img2.show()
   	img3 = Image.open("sellbuy.jpg")
   	img3.show()
   	dash()

   	print("Thank you for Contributing to our project! ")


        coven()

        i=1
        while i>0:
   	print("Select any one of the options below:")
   	print("1.Continue shopping")
   	print("2.View your recent products bought/sold")
   	print("3.Know more about our project")
        print("4.Exit application")
   	dash()
   	continue_ch=(input("Enter your choice:1/2/3/4"))
   	if continue_ch=="1":
   		coven()

   	elif continue_ch=="2":
        myStack = ['apple','banana','cabbage','maize','potato','wheat','onion']
        print("Current list is:")
        for i in range(len(myStack)):
    	print(i + 1, ".", myStack[i])

        wait_opt=input("Do you want to add or delete from the waiting list?A/D")
        if wait_opt=="a"or wait_opt=="A":
        add_prod=input("Enter the product you want to add to  the waiting list:")
            	myStack.append(add_prod)
    
        elif wait_opt=="d" or wait_opt=="D":
        	del_prod=int(input("Enter thenumber of the product you want to delete from the waiting list:"))
        	myStack.pop(del_prod-1)
        else:
        	print("Invalid Input!")
           	i=-1
                dash()
                print("Waiting list is:",myStack)


   	elif continue_ch=="3":
       		about()
       		final_ch=input("Would you like to shop/sell? Y/N")
       		if final_ch=="y" or final_ch=="Y":
           			coven()
		elif final_ch==’”n” or final_ch==”N”:
           			print("See you later!")
          			i=-1
		else:
			print(“Invalid Input!)

   	
        elif continue_ch=="4":
       		print("Thank you for using our application")
       		print("See you later!")
       		i=-1
   	
        else:
                print("Invalid Input!")
                i+=1



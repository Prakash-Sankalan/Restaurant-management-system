'''
CS PROJECT:FOOD ORDERING SYSTEM
CLASS XII-C
MADE BY- SHREYAN PRAKASH
''' 
'''
NAME OF RESTAURANT: ZAYKA
'''
import mysql.connector as m 
import bill   #Module created to display menu and calculate discount
db=m.connect(host="localhost", database="zayka_menu", user="root", passwd="$hrey@n13")
mc=db.cursor()
mc.execute("select * from starters")
st=mc.fetchall()
mc.execute("select * from beverages")
b=mc.fetchall()
mc.execute("select * from chineese")
ch=mc.fetchall()
mc.execute("select * from indian")
ind=mc.fetchall()
mc.execute("select * from continental")
co=mc.fetchall()
mc.execute("select * from dessert")
d=mc.fetchall()
mc.execute("select * from breads")
br=mc.fetchall()
mlst=[]    #Master list of items
olst=[]    #List of ordered items
ip=0       #Total initial price 
mlst.extend(st)
mlst.extend(b)
mlst.extend(br)
mlst.extend(ind)
mlst.extend(ch)
mlst.extend(co)
mlst.extend(d) 
for i in range(len(mlst)):    #To capitalize all the items in master list
    mlst[i]=list(mlst[i])
    mlst[i][1]=mlst[i][1].upper()
reply="YES"
print("\t\t\tWELCOME TO ZAYKA!!")  
while reply=="YES":         #Outermost while loop for navigation through menu  
    y=int(input("What would you like to do?\n1)View Menu\n2)Place Order\n3)View order list\n4)Checkout\n5)Remove item from order\n"))
    if y==1:
        x=input('''Please Follow the steps.\nTo View Starters, Enter st\nTo View Beverges, Enter b\nTo View breads, Enter br\nTo View main course, Enter mc\nTo View desserts, Enter d\nTo View The entire menu Enter me::\n''')
        if x=="st":
            print("\nSTARTERS:\n")
            bill.menu(st)
        elif x=="b":
            print("\nBEVERAGES:\ns")
            bill.menu(b)
        elif x=="br":
            print("\nBREADS:\n")
            bill.menu(br)
        elif x=="d":
            print("\nDESSERT:\n")
            bill.menu(d)
        elif x=="mc":
            print("MAIN COURSE:")
            print("\nCHINEESE:\n")
            bill.menu(ch)
            print("\nINDIAN:\n")
            bill.menu(ind)
            print("\nCONTINENTAL:\n")
            bill.menu(co)
        elif x=="me":
            print("\nSTARTERS:\n")
            bill.menu(st)
            print("\nBEVERAGES:\n")
            bill.menu(b)
            print("\nBREADS:\n")
            bill.menu(br)
            print("MAIN COURSE:")  
            print("\nCHINEESE:\n")
            bill.menu(ch)
            print("\nINDIAN:\n")
            bill.menu(ind)
            print("\nCONTINENTAL:\n")
            bill.menu(co)
            print("\nDESSERT:\n")  
            bill.menu(d)
        else:
            print("Enter a valid choice")
    elif y==2:
        for i in range(int(input("How many items would you like to order?"))):  #To place multiple items in order 
            o,q=input("Which item And quantity(Write separated by commas)::").split(",")
            o,q=o.upper(),int(q)
            for i in range(len(mlst)):    #To iterate through master list
                if mlst[i][1]==o:         #Checking if item exists  
                    for x in range(q):  #To add items in the order list
                        olst.append(mlst[i][1]) 
                        ip+=(mlst[i][-1])   #Adding to initial price
        print("Your order has been placed.")
    elif y==5:
        for i in range(int(input("How many items would you like to remove?"))):   #To remove multiple items 
            r,qr=input("Remove which item And quantity(Separated by commas)::").split(",")
            r,qr=r.upper(),int(qr)
            for i in range(len(mlst)):    #Iterating through master list
                if mlst[i][1]==r:
                    for x in range(qr):    #Iteration for multiple subtraction from initial price 
                        try:   
                            olst.remove(r)  #Removing qr number of times
                            ip-=mlst[i][-1]
                        except:   #If any entered condition is inconsistent
                            print("The quantity of the entered item has been exhausted OR It did not exist.")
    elif y==3:
        print("Your order is:\n" , olst)
        print("TOTAL AMOUNT:", ip)
    elif y==4:
        print("Your reciept is:", olst)
        print("YOUR TOTAL AMOUNT IS:", ip)      
        print("AMOUNT AFTER DISCOUNT:", bill.disc(ip))
    else:
        print("Enter a valid choice")
    reply=input("OPEN NAVIGATION AGAIN?::")
    reply=reply.upper()
else:     #loop else clause
    print("THANK YOU FOR DINING WITH US!")  #Concluding line
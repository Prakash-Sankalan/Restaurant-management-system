import mysql.connector as m
db=m.connect(host="localhost", database="zayka_menu", user="root", passwd="$hrey@n13")
mc=db.cursor()
mc.execute("select * from beverages")
x=input("Hello Customer, Please Follow the steps\nTo View Starters, Enter st\nTo View Bevarges, Enter b\nTo View breads, Enter br\nTo View maincource, Enter mc\nTo View desserts, enter d\nTo View The entire menu Enter y\n(To view either veg or nonveg add a v or nv before the command e.g nvst for nonveg starters)::")
if x=="y":
    print("beverages")
    for i in mc:
        print(i[0],i[1],i[2],sep="\t")
    mc.execute("select * from starters")
    print()
    print("starters")
    for i in mc:
        print(i[0],i[1],i[2],i[3],sep="\t")
    print()
    mc.execute("select * from chineese")
    print("chineese")
    for i in mc:
       print(i[0],i[1],i[2],sep="\t")
    print()
    mc.execute("select * from indian")
    print("indian")
    for i in mc:
        print(i[0],i[1],i[2],sep="\t")
    print()
    mc.execute("select * from continental")
    print("continental")
    for i in mc:
        print(i[0],i[1],i[2],sep="\t")
    print()
    mc.execute("select * from breads")
    print("breads")
    for i in mc:
        print(i[0],i[1],i[2],sep="\t")
    
    print()
    mc.execute("select * from dessert")
    print("desserts")
    for i in mc:
        print(i[0],i[1],i[2],sep="\t")
elif x=="st":
    mc.execute("select * from starters")
    for i in mc:
        print(i)
    




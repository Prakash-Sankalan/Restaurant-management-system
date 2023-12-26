# Restaurant-management-system
This project is based on python MySQL connectivity. It is an Electronic Food ordering system from a hypothetical restaurant “ZAYKA”. Originally created in 2019 as part of a project in Computer Science with Python for SSC 2019.
The project was made on a laptop with INTEL CORE i7 8th Gen and Windows 10 os. The python code was written on PYTHON 3.8 on SPYDER IDLE 64 bits but it can also be written in standard python IDLE 32 bit or 64 bit or on PYCHARM. Any version of MySQL greater than 5.7.2 may be used. The file mysql.connector must be installed. 
In the user interface following operations can be done:
(No case sensitivity wherever inputs are taken)
1. View Menu: The entire menu of the restaurant or 
section wise can be viewed.
2. Place order: Order of the required dishes from the menu 
can be placed. Multiple dishes and more than one 
quantity of a particular dish can be ordered at a time.
3. View order: The ordered dishes can be viewed in the 
form of a list and the total initial price is displayed.
4. Checkout: After ordering complete bill along with 
discounted price is displayed.
Discounting criteria is as follows:
If total price is greater than Rs5000.00 then 20% 
discount.
If total price is greater than Rs2000.00 and less than 
Rs5000.00 then 15% discount.
If total price is less than Rs2000.00 then 5% discount.
5. Remove item: An item from the ordered dishes can be 
removed. Multiple dishes and more than one quantity of 
a particular dish can be removed at a time.
The choices from the above mentioned tasks can be chosen as 
many times as required and toggling through the Menu can be 
done by typing “yes”.
To exit entering “no” is required.
MENU:
The menu of the restaurant is created in MySQL using simple 
SQL commands:
CREATE TABLE table_name (
 column1 datatype,
 column2 datatype,
 column3 datatype,
 ....
);
INSERT INTO table_name VALUES (
Value1, value2, …);
CONNECTION:
The python MySQL connection is established as 
follows
import mysql.connector
db=m.connect(host="localhost", database="zayka_menu", 
user="root", passwd="$hrey@n13")
mc=db.cursor()
Where mc is the cursor. Now any SQL command can 
be used as
mc.execute(“select * from table_name”)
MODULE:
A module named “bill” is created that has two functions:
i. disc(x): To calculate discount from the final value in 
accordance with the above mentioned conditions. It 
takes only one INT argument and has if-elif conditional 
statements and arithmetic operators.
ii. menu(x): It takes a list of tuples as input and iterates 
through it using a simple for loop and unpacks the tuple 
printing the unpacked values. In this program the list 
consists of tuples that are records from the tables in 
MySQL in the menu.
Tuple unpacking is done as follows:
print(*tuple[index])
DECLARATIONS:
Following variables are declared which are to be used later in 
the main program:
i. mc: The cursor for MySQL
ii. st: It stores the list of all the records from the table 
“starters” from the database.
Data from the table is retrieved using the fetchall() 
method as follows:
mc.execute("select * from starters")
st=mc.fetchall()
iii. b: It stores the list of all the records from the table 
“beverages” from the database.
Data from the table is retrieved in a similar manner as 
above.
iv. ch: It stores the list of all the records from the table 
“chineese” from the database.
Data from the table is retrieved in a similar manner as 
above
v. ind: It stores the list of all the records from the table 
“indian” from the database.
Data from the table is retrieved in a similar manner as 
above
vi. co: It stores the list of all the records from the table 
“continental” from the database.
Data from the table is retrieved in a similar manner as 
above
vii. d: It stores the list of all the records from the table 
“dessert” from the database.
Data from the table is retrieved in a similar manner as 
above
viii. br: It stores the list of all the records from the table 
“breads” from the database.
Data from the table is retrieved in a similar manner as 
above
ix. mlst: Empty list to store all the records from all the 
tables.
x. olst: Empty list to store placed orders.
xi. ip: Variable which will store the price, initially has 
value 0.
CREATING mlst:
For the ease of following codes in the program, a list of all the 
items from all the tables is created using the extend() 
method.
e.g mlst.extend(st) to store starters
Then to increase program efficiency by eliminating possibility 
of error due to case sensitivity, all the names are capitalized 
by iterating through the list using for loop and the 
string.upper() method as given from line 37-39.
MAIN CODE:
Code consists of a system where user can view menu, place 
order, delete order and view order. For this to occur as many 
times as user desires a while loop is applied with reply variable 
being “YES”. After every iteration the value of reply is updated 
and usingreply.upper()
The user has no restriction on case.
The navigation rules and options are printed to the user and 
accordingly conditional if-elif-else statements are made.
VIEWING MENU:
To display starters, beverages etc. each variable 
corresponding to each is printed using the menu function from 
bill module. One option to print all the items is also given and 
similar procedure is followed (As shown in output).
PLACING ORDER:
The code for placing order starts with a for loop that 
determines how many different types of items are to be 
added. Inside the loop using input.split() name and quantity of 
item is taken as input in variables o and q respectively (using 
upper() o is capitalized).
Then the mlst is iterated to check if item inputted is correct, if 
it matches any item from the list then another for loop which 
iterates q number of times is used which adds item in olst 
using olst.append(). Appropriate price is also added to ip.
REMOVING ORDER:
It is similar in code as placing order except for line 101 where 
a try and except block is added to deal with any inconsistency 
whatsoever.
Removal is done using remove() method. Appropriate price is 
also subtracted from ip.
VIEWING ORDER:
Order is displayed using simple print statement as in line 107 
and 108.
CHECKOUT:
Here also a simple print statement displays the order list and 
the discount is calculated using the disc() function from bill 
module.
When the while loop is terminated then a loop else clause is 
added which concludes the program.

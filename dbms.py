#DBMS PROJECT
#RESTAURANT MANAGEMENT SYSTEM 

#ANJALI DOFE (111903137)
#AMAN PATIL (111903135)
import mysql.connector

global mydb
global my_cursor

mydb = mysql.connector.connect(
	host = "localhost",
	user = "anjali",
	passwd = "dofe",
	database = "dbms_project"
	)

my_cursor = mydb.cursor()

def view_databases():
	my_cursor.execute("SHOW DATABASES")
	for table in my_cursor:
		print(table[0])

def create_table_jobs():
	my_cursor.execute("create table jobs(j_id int(5), j_title varchar(10), primary key(j_id))")

def describe_table_jobs():
	my_cursor.execute("describe jobs;")
	for row in my_cursor:
		print(row)

def jobs_description():
	print("+---------+-------------+------+-----+---------+-------+")
	print("| Field   | Type        | Null | Key | Default | Extra |")
	print("+---------+-------------+------+-----+---------+-------+")
	print("| j_id    | int         | NO   | PRI | NULL    |       |")
	print("| j_title | varchar(10) | YES  |     | NULL    |       |")
	print("+---------+-------------+------+-----+---------+-------+")

def create_table_employees():
	my_cursor.execute("create table employees(e_id int(7), e_name varchar(20) not null, e_phone varchar(11) not null, e_address varchar(25) not null, e_salary int(6), j_id int(5) not null, primary key(e_id), foreign key (j_id) references jobs(j_id));")

def employees_description():
	print("+-----------+-------------+------+-----+---------+-------+\n| Field     | Type        | Null | Key | Default | Extra |\n+-----------+-------------+------+-----+---------+-------+\n| e_id      | int         | NO   | PRI | NULL    |       |\n| e_name    | varchar(20) | NO   |     | NULL    |       |\n| e_phone   | varchar(11) | NO   |     | NULL    |       |\n| e_address | varchar(25) | NO   |     | NULL    |       |\n| e_salary  | int         | YES  |     | NULL    |       |\n| j_id      | int         | NO   | MUL | NULL    |       |\n+-----------+-------------+------+-----+---------+-------+")

def create_table_tables():
	my_cursor.execute("create table tables(t_id int(5), capacity int(2) not null, e_id int(7) not null, primary key(t_id), foreign key(e_id) references employees(e_id));")

def tables_description():
	print("+----------+------+------+-----+---------+-------+\n| Field    | Type | Null | Key | Default | Extra |\n+----------+------+------+-----+---------+-------+\n| t_id     | int  | NO   | PRI | NULL    |       |\n| capacity | int  | NO   |     | NULL    |       |\n| e_id     | int  | NO   | MUL | NULL    |       |\n+----------+------+------+-----+---------+-------+")

def create_table_food():
	my_cursor.execute("create table foods(f_id int(7), f_name varchar(10) unique, f_price int(5) not null, e_id int(7) not null, primary key(f_id), foreign key(e_id) references employees(e_id))")

def foods_description():
	print("+---------+-------------+------+-----+---------+-------+\n| Field   | Type        | Null | Key | Default | Extra |\n+---------+-------------+------+-----+---------+-------+\n| f_id    | int         | NO   | PRI | NULL    |       |\n| f_name  | varchar(10) | YES  | UNI | NULL    |       |\n| f_price | int         | NO   |     | NULL    |       |\n| e_id    | int         | NO   | MUL | NULL    |       |\n+---------+-------------+------+-----+---------+-------+")

def create_table_customers():
	my_cursor.execute("create table customers(c_id int(7), c_name varchar(20), c_phone varchar(11), c_address varchar(25), c_occupation varchar(6), primary key(c_id));")

def cutomers_description():
	print("+--------------+-------------+------+-----+---------+-------+\n| Field        | Type        | Null | Key | Default | Extra |\n+--------------+-------------+------+-----+---------+-------+\n| c_id         | int         | NO   | PRI | NULL    |       |\n| c_name       | varchar(20) | YES  |     | NULL    |       |\n| c_phone      | varchar(11) | YES  |     | NULL    |       |\n| c_address    | varchar(25) | YES  |     | NULL    |       |\n| c_occupation | varchar(10)  | YES  |     | NULL    |       |\n+--------------+-------------+------+-----+---------+-------+")

def create_table_orders():
	my_cursor.execute("create table orders(o_id int(7), o_type varchar(10), o_date date not null, c_id int(7), e_id int(7), primary key(o_id), foreign key(c_id) references customers(c_id), foreign key(e_id) references employees(e_id))")

def orders_description():
	print("+--------+-------------+------+-----+---------+-------+\n| Field  | Type        | Null | Key | Default | Extra |\n+--------+-------------+------+-----+---------+-------+\n| o_id   | int         | NO   | PRI | NULL    |       |\n| o_type | varchar(10) | YES  |     | NULL    |       |\n| o_date | date        | NO   |     | NULL    |       |\n| c_id   | int         | YES  | MUL | NULL    |       |\n| e_id   | int         | YES  | MUL | NULL    |       |\n+--------+-------------+------+-----+---------+-------+")

def create_table_order_history():
	my_cursor.execute("create table order_history(t_id int(5), o_id int(7), primary key(t_id,o_id), foreign key(t_id) references tables(t_id), foreign key(o_id) references orders(o_id))")

def create_table_items():
	my_cursor.execute("create table items(quantity int(4) not null, o_id int(7), f_id int(7), primary key(o_id,f_id), foreign key(o_id) references orders(o_id), foreign key(f_id) references foods(f_id))")

def create_table_booking():
	my_cursor.execute("create table booking(b_date date, b_hour int(2), c_id int(7), t_id int(5), primary key(c_id,t_id), foreign key(c_id) references customers(c_id), foreign key(t_id) references tables(t_id))")

def order_history_description():
	print("+-------+------+------+-----+---------+-------+\n| Field | Type | Null | Key | Default | Extra |\n+-------+------+------+-----+---------+-------+\n| t_id  | int  | NO   | PRI | NULL    |       |\n| o_id  | int  | NO   | PRI | NULL    |       |\n+-------+------+------+-----+---------+-------+")

def items_description():
	print("+----------+------+------+-----+---------+-------+\n| Field    | Type | Null | Key | Default | Extra |\n+----------+------+------+-----+---------+-------+\n| quantity | int  | NO   |     | NULL    |       |\n| o_id     | int  | NO   | PRI | NULL    |       |\n| f_id     | int  | NO   | PRI | NULL    |       |\n+----------+------+------+-----+---------+-------+")

def booking_description():
	print("+--------+------+------+-----+---------+-------+\n| Field  | Type | Null | Key | Default | Extra |\n+--------+------+------+-----+---------+-------+\n| b_date | date | YES  |     | NULL    |       |\n| b_hour | int  | YES  |     | NULL    |       |\n| c_id   | int  | NO   | PRI | NULL    |       |\n| t_id   | int  | NO   | PRI | NULL    |       |\n+--------+------+------+-----+---------+-------+")

def insert_jobs():
	try:
		#my_cursor = mydb.cursor()
		j_id = int(input("Enter job ID to be added to database (numeric): "))
		j_title = input("Enter job title for the above job ID: ")
		my_cursor.execute("insert into jobs(j_id, j_title) values({},'{}')".format(j_id, j_title))
		mydb.commit()
		print("Job added to database")
	except:
		print("Invalid data provided hence unable to add job to database")

def insert_customers():
	try:
		#my_cursor = mydb.cursor()
		c_id = int(input("Enter Customer ID to be added to database (numeric): "))
		c_name = input("Enter customer name for the above customer ID: ")
		c_phone = input("Enter customer's 10 digit phone number: ")
		c_address = input("Enter customer's address: ")
		c_occupation = input("Enter customer's occupation: ")
		my_cursor.execute("insert into customers(c_id, c_name, c_phone, c_address, c_occupation) values({},'{}','{}','{}','{}')".format(c_id, c_name, c_phone, c_address, c_occupation))
		mydb.commit()
		print("Customer added to database")
	except:
		print("Invalid data provided hence unable to add customer to database")

def insert_employees():
	try:
		e_id = int(input("Enter ID of employee: "))
		e_name = input("Enter employee name: ")
		e_phone = input("Enter 10 digit phone number of employee: ")
		e_address = input("Enter employee address: ")
		e_salary = int(input("Enter salary in Rupees: "))
		j_id = int(input("Enter job ID for employee: "))
		my_cursor.execute("insert into employees(e_id, e_name, e_phone, e_address, e_salary, j_id) values({},'{}','{}','{}',{},{})".format(e_id, e_name, e_phone, e_address, e_salary, j_id))
		mydb.commit()
		print("Employee added to database")
	except:
		print("Invalid data provided hence unable to add employee to database")

def show_jobs():
	my_cursor.execute("select * from jobs;")
	print("*********************************")
	print("Job ID\t\t\tJob Title")
	print("*********************************")
	for column in my_cursor:
		print(f" {column[0]}\t\t\t{column[1]}")

def show_employees():
	my_cursor.execute("select e_id,e_name,e_salary from employees;")
	print("*****************************************************************************")
	print("Employee ID\tEmployee Name\t\t Salary")
	print("*****************************************************************************")
	for column in my_cursor:
		#print(column)
		print(f" {column[0]}\t\t{column[1]}\t\t\t{column[2]}")


def show_customers():
	my_cursor.execute("select * from customers;")
	print("********************************************************************************")
	print("Customer ID\tCustomer Name\tPhone No.\tAddress  \tOccupation")
	print("********************************************************************************")
	for column in my_cursor:
		print(f" {column[0]}\t\t{column[1]}\t{column[2]}\t{column[3]}\t\t{column[4]}")


def insert_foods():
	try:
		f_id = int(input("Enter food ID: "))
		f_name = input("Enter name of dish: ")
		f_price = int(input("Enter price of food in Rupees: "))
		e_id = int(input("Enter employee ID cooking the dish: "))
		my_cursor.execute("insert into foods(f_id,f_name,f_price,e_id) values({},'{}',{},{})".format(f_id,f_name,f_price,e_id))
		mydb.commit()
		print("Food item added to database")
	except:
		print("Invalid data provided hence unable to add food dish")

def show_menu():
	my_cursor.execute("select f_id,f_name,f_price from foods;")
	print("******************************************************************")
	print("ID\t\tFood_Dish\tPrice(Rs)")
	print("******************************************************************")
	for column in my_cursor:
		print(f" {column[0]}\t\t{column[1]}\t\t{column[2]}")

def insert_tables():
	try:
		t_id = int(input("Enter table ID: "))
		capacity = int(input("Enter capacity: "))
		e_id = int(input("Enter employee ID maintaining table: "))
		my_cursor.execute("insert into tables values({},{},{})".format(t_id,capacity,e_id))
		mydb.commit()
		print("Successfully added tables to database")
	except:
		print("Invalid data provided unable to add table")

def show_tables():
	my_cursor.execute("select t_id,capacity from tables;")
	print("******************************************************************")
	print("ID\t\t  Capacity")
	print("******************************************************************")
	for column in my_cursor:
		print(f" {column[0]}\t\t\t{column[1]}")

def insert_booking():
	try:
		b_date = input("Enter date for booking(YYYY-MM-DD): ")
		b_hour = int(input("Enter hour of booking: "))
		c_id = int(input("Enter Customer ID: "))
		t_id = int(input("Enter Table ID for customer: "))
		my_cursor.execute("insert into booking values('{}',{},{},{})".format(b_date,b_hour,c_id,t_id))
		mydb.commit()
		print("Booking added")
	except:
		print("Invalid Data. Booking not added")

def insert_orders():
	try:
		o_id = int(input("Enter order ID: "))
		o_type = input("Order Type(Dine In/Takeaway/Online): ")
		o_date = input("Order date (YYYY-MM-DD): ")
		c_id = int(input("Customer ID: "))
		e_id = int(input("ID of employee handling order: "))
		my_cursor.execute("insert into orders values({},'{}','{}',{},{})".format(o_id,o_type,o_date,c_id,e_id))
		mydb.commit()
		print("Order added")
	except:
		print("Invalid order details provided")

def show_booking():
	my_cursor.execute("select * from booking;")
	print("******************************************************************")
	print("Date\t\tHour\tCustomer_ID\tTable_ID")
	print("******************************************************************")
	for column in my_cursor:
		print(f" {column[0]}\t{column[1]}\t\t{column[2]}\t\t{column[3]}")

def show_orders():
	my_cursor.execute("select * from orders;")
	print("******************************************************************")
	print("Order_ID\tOrder_Type\tO_Date\t\tCustomer_ID")
	print("******************************************************************")
	for column in my_cursor:
		print(f" {column[0]}\t\t{column[1]}\t{column[2]}\t{column[3]}")




if __name__ == "__main__":
	#view_databases()

	option = int(input(" Enter 1 to add jobs\n Enter 2 to add cutomers\n Enter 3 to add employees\n Enter 4 to add foods\n Enter 5 to add tables\n Enter 6 to add bookings\n Enter 7 to add orders\n Enter 8 to add items\n Enter 9 to add order history: "))

	if option == 1:
		insert_jobs()
	elif option == 2:
		insert_customers()
	elif option == 3:
		insert_employees()
	elif option == 4:
		insert_foods()
	elif option == 5:
		insert_tables()
	elif option == 6:
		insert_booking()
	elif option == 7:
		insert_orders()
	else:
		print("Invalid option")

	choice = int(input(" Enter 1 to show jobs\n Enter 2 to show customers\n Enter 3 to show employees\n Enter 4 to see menu\n Enter 5 to view tables\n Enter 6 to view bookings\n Enter 7 to view orders\n Enter 8 to view items\n Enter 9 to view order history:  "))
	if choice == 1:
		show_jobs()
	elif choice == 2:
		show_customers()
	elif choice == 3:
		show_employees()
	elif choice == 4:
		show_menu()
	elif choice == 5:
		show_tables()
	elif choice == 6:
		show_booking()
	elif choice == 7:
		show_orders()
	else:
		print("Thank you!!!")
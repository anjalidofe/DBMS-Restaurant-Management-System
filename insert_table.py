import mysql.connector
from rich.console import Console
import sys

console = Console()

global mydb
global my_cursor

mydb = mysql.connector.connect(
	host = "localhost",
	user = "anjali",
	passwd = "dofe",
	database = "dbms_project"
	)

my_cursor = mydb.cursor()

def insert_jobs():
	try:
		#my_cursor = mydb.cursor()
		j_id = int(input("Enter job ID to be added to database (numeric): "))
		j_title = input("Enter job title for the above job ID: ")
		my_cursor.execute("insert into jobs(j_id, j_title) values({},'{}')".format(j_id, j_title))
		mydb.commit()
		console.print("Job added to database", style = "bold red on white")
	except:
		console.print("Invalid data provided hence unable to add job to database",style = "bold red on white")

def insert_customers():
	try:
		#my_cursor = mydb.cursor()
		#c_id = int(input("Enter Customer ID to be added to database (numeric): "))
		c_name = input("Enter customer name for the above customer ID: ")
		c_phone = input("Enter customer's 10 digit phone number: ")
		c_address = input("Enter customer's address: ")
		c_occupation = input("Enter customer's occupation: ")
		my_cursor.execute("insert into customers(c_name, c_phone, c_address, c_occupation) values('{}','{}','{}','{}')".format(c_name, c_phone, c_address, c_occupation))
		mydb.commit()
		console.print("Customer added to database",style = "bold red on white")
	except:
		console.print("Invalid data provided hence unable to add customer to database", style = "bold red on white")

def insert_employees():
	try:
		#e_id = int(input("Enter ID of employee: "))
		e_name = input("Enter employee name: ")
		e_phone = input("Enter 10 digit phone number of employee: ")
		e_address = input("Enter employee address: ")
		e_salary = int(input("Enter salary in Rupees: "))
		j_id = int(input("Enter job ID for employee: "))
		my_cursor.execute("insert into employees(e_name, e_phone, e_address, e_salary, j_id) values('{}','{}','{}',{},{})".format(e_name, e_phone, e_address, e_salary, j_id))
		mydb.commit()
		console.print("Employee added to database",style = "bold red on white")
	except:
		console.print("Invalid data provided hence unable to add employee to database",style = "bold red on white")

def insert_foods():
	try:
		f_id = int(input("Enter food ID: "))
		f_name = input("Enter name of dish: ")
		f_price = int(input("Enter price of food in Rupees: "))
		e_id = int(input("Enter employee ID cooking the dish: "))
		my_cursor.execute("insert into foods(f_id,f_name,f_price,e_id) values({},'{}',{},{})".format(f_id,f_name,f_price,e_id))
		mydb.commit()
		console.print("Food item added to database",style = "bold red on white")
	except:
		console.print("Invalid data provided hence unable to add food dish",style = "bold red on white")

def insert_tables():
	try:
		#t_id = int(input("Enter table ID: "))
		capacity = int(input("Enter capacity: "))
		e_id = int(input("Enter employee ID maintaining table: "))
		my_cursor.execute("insert into tables(capacity, e_id) values({},{})".format(capacity,e_id))
		mydb.commit()
		console.print("Successfully added tables to database", style = "bold red on white")
	except:
		console.print("Invalid data provided unable to add table", style = "bold red on white")

def insert_booking():
	try:
		b_date = input("Enter date for booking(YYYY-MM-DD): ")
		b_hour = int(input("Enter hour of booking: "))
		c_id = int(input("Enter Customer ID: "))
		t_id = int(input("Enter Table ID for customer: "))
		my_cursor.execute("insert into booking values('{}',{},{},{})".format(b_date,b_hour,c_id,t_id))
		mydb.commit()
		console.print("Booking added",style = "bold red on white")
	except:
		console.print("Invalid Data. Booking not added",style = "bold red on white")

def insert_orders():
	try:
		o_id = int(input("Enter order ID: "))
		o_type = input("Order Type(Dine In/Takeaway/Online): ")
		o_date = input("Order date (YYYY-MM-DD): ")
		c_id = int(input("Customer ID: "))
		e_id = int(input("ID of employee handling order: "))
		my_cursor.execute("insert into orders values({},'{}','{}',{},{})".format(o_id,o_type,o_date,c_id,e_id))
		mydb.commit()
		console.print("Order added",style = "bold red on white")
	except:
		console.print("Invalid order details provided",style = "bold red on white")

def insert_items():
	try:
		o_id = int(input("Enter orderID: "))
		f_id = int(input("Enter foodID: "))
		quantity = int(input("Enter quantity: "))
		my_cursor.execute("insert into items values({},{},{})".format(quantity,o_id,f_id))
		mydb.commit()
		console.print("Items added to order",style = "bold red on white")
	except:
		console.print("Incorrect item details provided",style = "bold red on white")

def insert_order_history():
	try:
		t_id = int(input("Enter Table ID: "))
		o_id = int(input("Enter order ID: "))
		my_cursor.execute("Insert into order_history values({},{})".format(t_id, o_id))
		mydb.commit()
		console.print("Successfully added",style = "bold red on white")
	except:
		console.print("Invalid data provided",style = "bold red on white")

if __name__ == "__main__":

	while True:

		console.print(" Enter 1 to add jobs\n Enter 2 to add cutomers\n Enter 3 to add employees\n Enter 4 to add foods\n Enter 5 to add tables\n Enter 6 to add bookings\n Enter 7 to add orders\n Enter 8 to add items\n Enter 9 to add order history \n Enter any other key to exit",style = "bold blue")
		option = int(input(" Your Choice: "))
		print("\n")
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
		elif option == 8:
			insert_items()
		elif option == 9:
			insert_order_history()
		else:
			console.print("Exiting the program", style = "bold red")
			sys.exit(0)
		print("\n")

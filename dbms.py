#DBMS PROJECT
#RESTAURANT MANAGEMENT SYSTEM 

#ANJALI DOFE (111903137)
#AMAN PATIL (111903135)
import mysql.connector
from rich.console import Console
from rich.table import Table
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

def view_databases():
	my_cursor.execute("SHOW DATABASES")
	for table in my_cursor:
		print(table[0])

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

def employees_description():
	console.print("+-----------+-------------+------+-----+---------+----------------+\n| Field     | Type        | Null | Key | Default | Extra          |\n+-----------+-------------+------+-----+---------+----------------+\n| e_id      | int         | NO   | PRI | NULL    | auto_increment |\n| e_name    | varchar(20) | NO   |     | NULL    |                |\n| e_phone   | varchar(11) | NO   |     | NULL    |                |\n| e_address | varchar(25) | NO   |     | NULL    |                |\n| e_salary  | int         | YES  |     | NULL    |                |\n| j_id      | int         | NO   | MUL | NULL    |                |\n+-----------+-------------+------+-----+---------+----------------+", style = "bold blue")

def tables_description():
	console.print("+----------+------+------+-----+---------+-------+\n| Field    | Type | Null | Key | Default | Extra |\n+----------+------+------+-----+---------+-------+\n| t_id     | int  | NO   | PRI | NULL    |       |\n| capacity | int  | NO   |     | NULL    |       |\n| e_id     | int  | NO   | MUL | NULL    |       |\n+----------+------+------+-----+---------+-------+", style = "bold pink")

def foods_description():
	print("+---------+-------------+------+-----+---------+-------+\n| Field   | Type        | Null | Key | Default | Extra |\n+---------+-------------+------+-----+---------+-------+\n| f_id    | int         | NO   | PRI | NULL    |       |\n| f_name  | varchar(10) | YES  | UNI | NULL    |       |\n| f_price | int         | NO   |     | NULL    |       |\n| e_id    | int         | NO   | MUL | NULL    |       |\n+---------+-------------+------+-----+---------+-------+")

def cutomers_description():
	print("+--------------+-------------+------+-----+---------+-------+\n| Field        | Type        | Null | Key | Default | Extra |\n+--------------+-------------+------+-----+---------+-------+\n| c_id         | int         | NO   | PRI | NULL    |       |\n| c_name       | varchar(20) | YES  |     | NULL    |       |\n| c_phone      | varchar(11) | YES  |     | NULL    |       |\n| c_address    | varchar(25) | YES  |     | NULL    |       |\n| c_occupation | varchar(10)  | YES  |     | NULL    |       |\n+--------------+-------------+------+-----+---------+-------+")

def orders_description():
	print("+--------+-------------+------+-----+---------+-------+\n| Field  | Type        | Null | Key | Default | Extra |\n+--------+-------------+------+-----+---------+-------+\n| o_id   | int         | NO   | PRI | NULL    |       |\n| o_type | varchar(10) | YES  |     | NULL    |       |\n| o_date | date        | NO   |     | NULL    |       |\n| c_id   | int         | YES  | MUL | NULL    |       |\n| e_id   | int         | YES  | MUL | NULL    |       |\n+--------+-------------+------+-----+---------+-------+")

def order_history_description():
	print("+-------+------+------+-----+---------+-------+\n| Field | Type | Null | Key | Default | Extra |\n+-------+------+------+-----+---------+-------+\n| t_id  | int  | NO   | PRI | NULL    |       |\n| o_id  | int  | NO   | PRI | NULL    |       |\n+-------+------+------+-----+---------+-------+")

def items_description():
	print("+----------+------+------+-----+---------+-------+\n| Field    | Type | Null | Key | Default | Extra |\n+----------+------+------+-----+---------+-------+\n| quantity | int  | NO   |     | NULL    |       |\n| o_id     | int  | NO   | PRI | NULL    |       |\n| f_id     | int  | NO   | PRI | NULL    |       |\n+----------+------+------+-----+---------+-------+")

def booking_description():
	print("+--------+------+------+-----+---------+-------+\n| Field  | Type | Null | Key | Default | Extra |\n+--------+------+------+-----+---------+-------+\n| b_date | date | YES  |     | NULL    |       |\n| b_hour | int  | YES  |     | NULL    |       |\n| c_id   | int  | NO   | PRI | NULL    |       |\n| t_id   | int  | NO   | PRI | NULL    |       |\n+--------+------+------+-----+---------+-------+")

def show_jobs():
	my_cursor.execute("select * from jobs;")
	table = Table(show_header=True, header_style="bold magenta")
	table.add_column("[green]Job ID[/green]", style="dim", width=12)
	table.add_column("[yellow]Job Title[/yellow]")
	for column in my_cursor:
		table.add_row(f"[green]{column[0]}[/green]",f"[yellow]{column[1]}[/yellow]")
	console.print(table)
	# print("*********************************")
	# print("Job ID\t\t\tJob Title")
	# print("*********************************")
	# for column in my_cursor:
	# 	print(f" {column[0]}\t\t\t{column[1]}")

def show_employees():
	my_cursor.execute("select e_id,e_name,e_salary,jobs.j_title from employees, jobs where jobs.j_id = employees.j_id;")
	table = Table(show_header=True, header_style="bold magenta")
	table.add_column("[blue]Employee ID[/blue]", style="dim", width=12)
	table.add_column("[blue]Employee Name[/blue]")
	table.add_column("[blue]Salary[/blue]", justify="left")
	table.add_column("[blue]Job Title[/blue]")
	for column in my_cursor:
		table.add_row(f"[blue]{column[0]}[/blue]", f"[blue]{column[1]}[/blue]",f"[blue]Rs.{column[2]}[/blue]",f"[blue]{column[3]}[/blue]")
	console.print(table)
	# print("*****************************************************************************")
	# print("Employee ID\tEmployee Name\t\t Salary")
	# print("*****************************************************************************")
	# for column in my_cursor:
	# 	#print(column)
	# 	print(f" {column[0]}\t\t{column[1]}\t\t\t{column[2]}")

def show_customers():
	my_cursor.execute("select * from customers;")
	table = Table(show_header=True, header_style="bold magenta")
	table.add_column("[blue]Customer ID[/blue]", style="dim", width=12)
	table.add_column("[blue]Customer Name[/blue]")
	table.add_column("[blue]Phone Number[/blue]")
	table.add_column("[blue]Address[/blue]")
	table.add_column("[blue]Occupation[/blue]")
	for column in my_cursor:
		table.add_row(f"[blue]{column[0]}[/blue]", f"[blue]{column[1]}[/blue]",f"[blue]{column[2]}[/blue]",f"[blue]{column[3]}[/blue]",f"[blue]{column[4]}[/blue]")
	console.print(table)
	# print("********************************************************************************")
	# print("Customer ID\tCustomer Name\tPhone No.\tAddress  \tOccupation")
	# print("********************************************************************************")
	# for column in my_cursor:
	# 	print(f" {column[0]}\t\t{column[1]}\t{column[2]}\t{column[3]}\t\t{column[4]}")

def show_menu():
	my_cursor.execute("select f_id,f_name,f_price from foods;")
	table = Table(show_header=True, header_style="bold magenta")
	table.add_column("[green]Food ID[/green]", style="dim", width=12)
	table.add_column("[green]Dish[/green]")
	table.add_column("[green]Price[/green]", justify="left")
	for column in my_cursor:
		table.add_row(f"[green]{column[0]}[/green]", f"[green]{column[1]}[/green]",f"[blue]Rs.{column[2]}[/blue]")
	console.print(table)
	# console.print("******************************************************************", style = "bold red on white")
	# console.print("ID\t\tFood_Dish\tPrice(Rs)", style = "bold white")
	# console.print("******************************************************************", style = "bold red on white")
	# for column in my_cursor:
	# 	console.print(f" {column[0]}\t\t{column[1]}\t\t{column[2]}", style = "bold white")

def show_tables():
	my_cursor.execute("select t_id,capacity from tables;")
	table = Table(show_header=True, header_style="bold magenta")
	table.add_column("[green]Table ID[/green]", style="dim", width=12)
	table.add_column("[yellow]Table Capacity[/yellow]")
	for column in my_cursor:
		table.add_row(f"[green]{column[0]}[/green]",f"[yellow]{column[1]}[/yellow]")
	console.print(table)
	# print("******************************************************************")
	# print("ID\t\t  Capacity")
	# print("******************************************************************")
	# for column in my_cursor:
	# 	print(f" {column[0]}\t\t\t{column[1]}")

def show_booking():
	my_cursor.execute("select b_date, b_hour, customers.c_name from booking, customers where customers.c_id = booking.c_id;")
	table = Table(show_header=True, header_style="bold magenta")
	table.add_column("[green]Booking Date[/green]", style="dim", width=12)
	table.add_column("[green]Time(in PM)[/green]")
	table.add_column("[green]Booked by Customer[/green]", justify="left")
	for column in my_cursor:
		table.add_row(f"[green]{column[0]}[/green]", f"[green]{column[1]}[/green]",f"[blue]{column[2]}[/blue]")
	console.print(table)
	# print("******************************************************************")
	# print("Date\t\tHour\tCustomer_ID\tTable_ID")
	# print("******************************************************************")
	# for column in my_cursor:
	# 	print(f" {column[0]}\t{column[1]}\t\t{column[2]}\t\t{column[3]}")

def show_orders():
	my_cursor.execute("select * from orders;")
	table = Table(show_header=True, header_style="bold magenta")
	table.add_column("[blue]Order ID[/blue]", style="dim", width=12)
	table.add_column("[blue]Order Type[/blue]")
	table.add_column("[blue]Order Date[/blue]", justify="left")
	table.add_column("[blue]Customer ID[/blue]")
	for column in my_cursor:
		table.add_row(f"[blue]{column[0]}[/blue]", f"[blue]{column[1]}[/blue]",f"[blue]{column[2]}[/blue]",f"[blue]{column[3]}[/blue]")
	console.print(table)
	# print("******************************************************************")
	# print("Order_ID\tOrder_Type\tO_Date\t\tCustomer_ID")
	# print("******************************************************************")
	# for column in my_cursor:
	# 	print(f" {column[0]}\t\t{column[1]}\t{column[2]}\t{column[3]}")

def show_items():
	my_cursor.execute("select o_id, foods.f_name, quantity from items, foods where foods.f_id = items.f_id;")
	table = Table(show_header=True, header_style="bold magenta")
	table.add_column("[green]Order ID[/green]", style="dim", width=12)
	table.add_column("[green]Food Ordered[/green]")
	table.add_column("[green]Quantity[/green]", justify="left")
	for column in my_cursor:
		table.add_row(f"[green]{column[0]}[/green]", f"[green]{column[1]}[/green]",f"[blue]{column[2]}[/blue]")
	console.print(table)
	# print("******************************************************************")
	# print("OrderID\tFood_ID\tQuantity")
	# print("******************************************************************")
	# for column in my_cursor:
	# 	print(f" {column[0]}\t\t{column[1]}\t\t{column[2]}")

def show_order_history():
	my_cursor.execute("select * from order_history;")
	table = Table(show_header=True, header_style="bold magenta")
	table.add_column("[green]Table ID[/green]", style="dim", width=12)
	table.add_column("[yellow]Order ID[/yellow]")
	for column in my_cursor:
		table.add_row(f"[green]{column[0]}[/green]",f"[yellow]{column[1]}[/yellow]")
	console.print(table)
	# print("******************************************************************")
	# print("Table_ID\tOrder_ID")
	# print("******************************************************************")
	# for column in my_cursor:
	# 	print(f" {column[0]}\t\t{column[1]}")


if __name__ == "__main__":
	#view_databases()
	while True:
		print()
		console.print(" Enter 1 to show jobs\n Enter 2 to show customers\n Enter 3 to show employees\n Enter 4 to see menu\n Enter 5 to view tables\n Enter 6 to view bookings\n Enter 7 to view orders\n Enter 8 to view items\n Enter 9 to view order history\n Enter any other key to EXIT ", style = "bold italic purple")
		print()
		choice = int(input(" Your choice : "))
		print()
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
		elif choice == 8:
			show_items()
		elif choice == 9:
			show_order_history()
		else:
			console.print(" Thank you!!!", style = "bold red")
			sys.exit()
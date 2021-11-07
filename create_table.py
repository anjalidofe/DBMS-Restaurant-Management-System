import mysql.connector
from rich.console import Console

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

def create_table_jobs():
	my_cursor.execute("create table jobs(j_id int(5), j_title varchar(10), primary key(j_id))")

def create_table_employees():
	my_cursor.execute("create table employees(e_id int(7) AUTO_INCREMENT, e_name varchar(20) not null, e_phone varchar(11) not null, e_address varchar(25) not null, e_salary int(6), j_id int(5) not null, primary key(e_id), foreign key (j_id) references jobs(j_id));")

def create_table_tables():
	my_cursor.execute("create table tables(t_id int(5) AUTO_INCREMENT, capacity int(2) not null, e_id int(7) not null, primary key(t_id), foreign key(e_id) references employees(e_id));")

def create_table_food():
	my_cursor.execute("create table foods(f_id int(7) AUTO_INCREMENT, f_name varchar(10) unique, f_price int(5) not null, e_id int(7) not null, primary key(f_id), foreign key(e_id) references employees(e_id))")

def create_table_customers():
	my_cursor.execute("create table customers(c_id int(7) AUTO_INCREMENT, c_name varchar(20), c_phone varchar(11), c_address varchar(25), c_occupation varchar(10), primary key(c_id));")

def create_table_orders():
	my_cursor.execute("create table orders(o_id int(7) AUTO_INCREMENT, o_type varchar(10), o_date date not null, c_id int(7), e_id int(7), primary key(o_id), foreign key(c_id) references customers(c_id), foreign key(e_id) references employees(e_id))")

def create_table_order_history():
	my_cursor.execute("create table order_history(t_id int(5), o_id int(7), primary key(t_id,o_id), foreign key(t_id) references tables(t_id), foreign key(o_id) references orders(o_id))")

def create_table_items():
	my_cursor.execute("create table items(quantity int(4) not null, o_id int(7), f_id int(7), primary key(o_id,f_id), foreign key(o_id) references orders(o_id), foreign key(f_id) references foods(f_id))")

def create_table_booking():
	my_cursor.execute("create table booking(b_date date, b_hour int(2), c_id int(7), t_id int(5), primary key(c_id,t_id), foreign key(c_id) references customers(c_id), foreign key(t_id) references tables(t_id))")

if __name__ == "__main__":

	#create_table_jobs()
	#create_table_employees()
	#create_table_tables()
	#create_table_food()
	#create_table_customers()
	#create_table_orders()
	#create_table_order_history()
	#create_table_items()
	#create_table_booking()

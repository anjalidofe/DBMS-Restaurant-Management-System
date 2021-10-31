#MIS 111903137
#MIS 111903135

#This python file contains code to drop tables

import mysql.connector

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

def drop_booking():
	my_cursor.execute("DROP TABLE booking;")

def drop_items():
	my_cursor.execute("DROP TABLE items;")

def drop_order_history():
	my_cursor.execute("DROP TABLE order_history;")

def drop_orders():
	my_cursor.execute("DROP TABLE orders;")

def drop_customers():
	my_cursor.execute("DROP TABLE customers;")

def drop_food():
	my_cursor.execute("DROP TABLE foods;")

def drop_tables():
	my_cursor.execute("DROP TABLE tables;")

def drop_employees():
	my_cursor.execute("DROP TABLE employees;")

def drop_jobs():
	my_cursor.execute("DROP TABLE jobs;")
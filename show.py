from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk 
import mysql.connector
from tkinter import ttk
from types import resolve_bases

root = Tk()
root.title("Restaurant Management System - DBMS")
root.geometry("650x500")
root.configure(bg ="#031163")

mydb = mysql.connector.connect(
	host = "localhost",
	user = "anjali",
	passwd = "dofe",
	database = "dbms_project"
	)
#creating cursor and initializing it
my_cursor = mydb.cursor()

#clear date function
def clear_date():
	date_box.delete(0, END)

#view sales of a particular date
def view_sales():
	date = date_box.get()
	list_sales_query = Tk()
	list_sales_query.title(f"Sales on {date}")
	list_sales_query.geometry("500x100")
	list_sales_query.configure(bg = "pink")
	my_cursor.execute("SELECT SUM(f.f_price*i.quantity) FROM foods f, items i where i.f_id = f.f_id AND i.o_id IN (SELECT o_id FROM orders o WHERE o_date = '{}');".format(date))
	result = my_cursor.fetchall()
	text_label = Label(list_sales_query,text="Total Sales on "+date+" are:",font = ("Helvetica",16),fg= "#070e57").grid(row = 1, column= 1,columnspan = 2,padx=5,pady=5)
	for x in result:
		lookup_label = Label(list_sales_query, text="Rs."+str(x[0]),font = ("Helvetica",16),fg= "#070e57")
		lookup_label.grid(row=1,column=3,padx=5,pady=5)
	clear_date()

def view_expenses():
	list_expenses_query = Tk()
	list_expenses_query.title(f"Expenses on employees")
	list_expenses_query.geometry("200x200")
	list_expenses_query.configure(bg = "pink")
	my_cursor.execute("SELECT j_title Job, SUM(e_salary) Expenses from employees NATURAL JOIN jobs GROUP BY j_title;")
	result = my_cursor.fetchall()
	text_label = Label(list_expenses_query,text="JOB",font = ("Helvetica",16),fg= "#070e57",bg="#7ddae8").grid(row = 1, column= 1,padx=5,pady=5)
	text2_label = Label(list_expenses_query,text="Expenses",font = ("Helvetica",16),fg= "#070e57",bg="#7ddae8").grid(row = 1, column= 2,padx=5,pady=5)
	num = 2
	for x in result:
		lookup_label = Label(list_expenses_query, text=x[0],font = ("Helvetica",16),fg= "#070e57")
		lookup_label.grid(row=num,column=1,padx=5,pady=5)
		lookup2_label = Label(list_expenses_query, text="Rs."+ str(x[1]),font = ("Helvetica",16),fg= "#070e57")
		lookup2_label.grid(row=num,column=2,padx=5,pady=5)
		num+=1

def total_expenses():
	list_total_query = Tk()
	list_total_query.title(f"Total Employee Expenses")
	list_total_query.geometry("600x100")
	list_total_query.configure(bg = "pink")
	my_cursor.execute("SELECT SUM(e_salary) FROM employees;")
	result = my_cursor.fetchall()
	text_label = Label(list_total_query,text="Total expenses of Restaurant on employees are:",font = ("Helvetica",16),fg= "#070e57").grid(row = 1, column= 1,columnspan = 2,padx=5,pady=5)
	for x in result:
		lookup_label = Label(list_total_query, text="Rs."+str(x[0]),font = ("Helvetica",16),fg= "#070e57")
		lookup_label.grid(row=1,column=3,padx=5,pady=5)

def total_bill():
	list_bill_query = Tk()
	list_bill_query.title(f"Customer Bills")
	list_bill_query.geometry("300x350")
	list_bill_query.configure(bg = "pink")
	my_cursor.execute("SELECT c.c_name, SUM(f.f_price*i.quantity) FROM customers c, foods f, items i, orders o WHERE c.c_id = o.c_id AND o.o_id = i.o_id AND i.f_id = f.f_id GROUP BY c.c_id;")
	result = my_cursor.fetchall()
	text_label = Label(list_bill_query,text="Customer Name",font = ("Helvetica",16),fg= "#070e57",bg="#7ddae8").grid(row = 1, column= 1,padx=5,pady=5)
	text2_label = Label(list_bill_query,text="BILL",font = ("Helvetica",16),fg= "#070e57",bg="#7ddae8").grid(row = 1, column= 2,padx=5,pady=5)
	num = 2
	for x in result:
		lookup_label = Label(list_bill_query, text=x[0],font = ("Helvetica",16),fg= "#070e57")
		lookup_label.grid(row=num,column=1,padx=5,pady=5)
		lookup2_label = Label(list_bill_query, text="Rs."+ str(x[1]),font = ("Helvetica",16),fg= "#070e57")
		lookup2_label.grid(row=num,column=2,padx=5,pady=5)
		num+=1

def best():
	best_query = Tk()
	best_query.title(f"Best Selling Dish")
	best_query.geometry("550x100")
	best_query.configure(bg = "pink")
	my_cursor.execute("select sum(quantity), f_name from foods,items where items.f_id = foods.f_id group by foods.f_id order by sum(quantity) desc LIMIT 1;")
	result = my_cursor.fetchall()
	text_label = Label(best_query,text="The Best Selling Dish of the Restaurant:",font = ("Helvetica",16),fg= "#070e57").grid(row = 1, column= 1,columnspan = 2,padx=5,pady=5)
	for x in result:
		lookup_label = Label(best_query, text=x[1],font = ("Helvetica",16),fg= "#070e57")
		lookup_label.grid(row=1,column=3,padx=5,pady=5)

def least():
	least_query = Tk()
	least_query.title(f"Least Selling Dish")
	least_query.geometry("550x100")
	least_query.configure(bg = "pink")
	my_cursor.execute("select sum(quantity), f_name from foods,items where items.f_id = foods.f_id group by foods.f_id order by sum(quantity) LIMIT 1;")
	result = my_cursor.fetchall()
	text_label = Label(least_query,text="The least selling dish of the restaurant:",font = ("Helvetica",16),fg= "#070e57").grid(row = 1, column= 1,columnspan = 2,padx=5,pady=5)
	for x in result:
		lookup_label = Label(least_query, text=x[1],font = ("Helvetica",16),fg= "#070e57")
		lookup_label.grid(row=1,column=3,padx=5,pady=5)


# bg = PhotoImage(file ="D:/SEMESTER 5/DBMS/Project/bgg.png")

# bg1 = Label(root , image=bg).place(x=0,y=0 , relwidth=1 , relheight=1)
#create a Label
title_label = Label(root, text = "Restaurant Management System Quick Lookup", font = ("Helvetica",18), fg= "#070e57", bg = "#7ddae8")
title_label.grid(row=0,column=0,columnspan=3,pady="20")

#create Main Form
total_sales_date_label = Label(root,text="Total Sales on Date (YYYY-MM-DD)", font = ("Helvetica", 14)).grid(row=1,column=0,columnspan=2, sticky=W,padx=10)
#create entry box
date_box = Entry(root, font=("Helvetica",14), fg="#073457",bg="#7ddae8")
date_box.grid(row=1,column=2)

#Create Buttons
view_sales_button = Button(root,text="View Sales",font = ("Helvetica",15),fg="#073457",bg="#7ddae8",command=view_sales)
view_sales_button.grid(row=14,column=1,padx=10,pady=10)
clear_date_button = Button(root,text="Clear Date",font = ("Helvetica",15),fg="#073457",bg="#7ddae8",command=clear_date)
clear_date_button.grid(row=14,column=2,padx=10,pady=10)

view_jobwise_expense_button = Button(root,text="View Jobwise Employee Expenses",font=("Helvetica",15),fg="#073457",bg="#7ddae8",command=view_expenses)
view_jobwise_expense_button.grid(row=15,column=1,columnspan=2,padx=10,pady=10)

view_total_expense_button = Button(root,text="View Total Expenses for Employee",font=("Helvetica",15),fg="#073457",bg="#7ddae8",command=total_expenses)
view_total_expense_button.grid(row=16,column=1,columnspan=2,padx=10,pady=10)

view_bill_button = Button(root,text="View the Total Bill for all Customers",font=("Helvetica",15),fg="#073457",bg="#7ddae8",command=total_bill)
view_bill_button.grid(row=17,column=1,columnspan=2,padx=10,pady=10)

best_button = Button(root,text="View the best selling food Dish here",font=("Helvetica",15),fg="#073457",bg="#7ddae8",command=best)
best_button.grid(row=18,column=1,columnspan=2,padx=10,pady=10)

least_button = Button(root,text="View the least selling food Dish here",font=("Helvetica",15),fg="#073457",bg="#7ddae8",command=least)
least_button.grid(row=19,column=1,columnspan=2,pady=10)

root.mainloop()
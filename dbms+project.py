#DBMS PROJECT
#RESTAURANT MANAGEMENT SYSTEM 

#ANJALI DOFE (111903137)
#AMAN PATIL (111903135)

from types import resolve_bases
import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk



mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "amanrajput90",
	database = "dbms_project"
	)

my_cursor = mydb.cursor()

def view_databases():
	
	my_cursor.execute("SHOW DATABASES")
	for table in my_cursor:
		print(table[0])

def create_table_jobs():
	global my_cursor 
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
	my_cursor.execute("create table employees(e_id int(7) AUTO_INCREMENT, e_name varchar(20) not null, e_phone varchar(11) not null, e_address varchar(25) not null, e_salary int(6), j_id int(5) not null, primary key(e_id), foreign key (j_id) references jobs(j_id));")

def employees_description():
	print("+-----------+-------------+------+-----+---------+-------+\n| Field     | Type        | Null | Key | Default | Extra |\n+-----------+-------------+------+-----+---------+-------+\n| e_id      | int         | NO   | PRI | NULL    |       |\n| e_name    | varchar(20) | NO   |     | NULL    |       |\n| e_phone   | varchar(11) | NO   |     | NULL    |       |\n| e_address | varchar(25) | NO   |     | NULL    |       |\n| e_salary  | int         | YES  |     | NULL    |       |\n| j_id      | int         | NO   | MUL | NULL    |       |\n+-----------+-------------+------+-----+---------+-------+")

def create_table_tables():
	my_cursor.execute("create table tables(t_id int(5) AUTO_INCREMENT , capacity int(2) not null, e_id int(7) not null, primary key(t_id), foreign key(e_id) references employees(e_id));")

def tables_description():
	print("+----------+------+------+-----+---------+-------+\n| Field    | Type | Null | Key | Default | Extra |\n+----------+------+------+-----+---------+-------+\n| t_id     | int  | NO   | PRI | NULL    |       |\n| capacity | int  | NO   |     | NULL    |       |\n| e_id     | int  | NO   | MUL | NULL    |       |\n+----------+------+------+-----+---------+-------+")

def create_table_food():
	my_cursor.execute("create table foods(f_id int(7), f_name varchar(10) unique, f_price int(5) not null, e_id int(7) not null, primary key(f_id), foreign key(e_id) references employees(e_id))")

def foods_description():
	print("+---------+-------------+------+-----+---------+-------+\n| Field   | Type        | Null | Key | Default | Extra |\n+---------+-------------+------+-----+---------+-------+\n| f_id    | int         | NO   | PRI | NULL    |       |\n| f_name  | varchar(10) | YES  | UNI | NULL    |       |\n| f_price | int         | NO   |     | NULL    |       |\n| e_id    | int         | NO   | MUL | NULL    |       |\n+---------+-------------+------+-----+---------+-------+")

def create_table_customers():
	my_cursor.execute("create table customers(c_id int(7)AUTO_INCREMENT , c_name varchar(20), c_phone varchar(11), c_address varchar(25), c_occupation varchar(6), primary key(c_id));")

def cutomers_description():
	print("+--------------+-------------+------+-----+---------+-------+\n| Field        | Type        | Null | Key | Default | Extra |\n+--------------+-------------+------+-----+---------+-------+\n| c_id         | int         | NO   | PRI | NULL    |       |\n| c_name       | varchar(20) | YES  |     | NULL    |       |\n| c_phone      | varchar(11) | YES  |     | NULL    |       |\n| c_address    | varchar(25) | YES  |     | NULL    |       |\n| c_occupation | varchar(6)  | YES  |     | NULL    |       |\n+--------------+-------------+------+-----+---------+-------+")

def create_table_orders():
	my_cursor.execute("create table orders(o_id int(7) AUTO_INCREMENT, o_type varchar(10), o_date date not null, c_id int(7), e_id int(7), primary key(o_id), foreign key(c_id) references customers(c_id), foreign key(e_id) references employees(e_id))")

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

def customer(frame1):
	customer_f = Frame(frame1 , bg = "white")
	customer_f.place(x= 152 , y = 50 , relwidth= 1 , height= 450 )
	lab1 = Label(customer_f , text ="Name     : "  , font=("ALGERIAN" , 15) , bg  = "white", anchor="w" ) 
	lab1.place(x=0 , y = 0 , width = 200 , height = 20)
	e1 = Entry(customer_f, bg = "#eee5de"  )
	e1.place(x=300 , y =0 , height= 20 , width = 140 )
	lab2 = Label(customer_f , text ="Address          :  " ,  font=("ALGERIAN" , 15) , bg = "white" ,anchor="w") 
	lab2.place(x=0 , y = 40 , width = 200 , height = 20)
	e2 = Entry(customer_f, bg = "#eee5de"  )
	e2.place(x=300 , y =40, height= 20 , width = 140 )
	lab3 = Label(customer_f , text ="Phone Number  :  ",  font=("ALGERIAN" , 15) , bg = "white" , anchor="w" ) 
	lab3.place(x=0 , y = 80 , width = 200 , height = 20)
	e3 = Entry(customer_f, bg = "#eee5de"  )
	e3.place(x=300 , y =80, height= 20 , width = 140 )
	lab4 = Label(customer_f , text ="Occupation      :  ",  font=("ALGERIAN" , 15) , bg  = "white" , anchor="w" ) 
	lab4.place(x=0 , y = 120 , width = 200 , height = 20)
	e4 = Entry(customer_f, bg = "#eee5de"  )
	e4.place(x=300, y =120 , height= 20 , width = 140 )
	lab5 = Label(customer_f , text ="Date       : ",  font=("ALGERIAN" , 15) , bg  = "white" , anchor="w" ) 
	lab5.place(x=0 , y = 160 , width = 200 , height = 20)
	e5 = Entry(customer_f, bg = "#eee5de"  )
	e5.place(x=300 , y = 160, height= 20 , width = 140 )
	lab6 = Label(customer_f , text ="Hour       : ",  font=("ALGERIAN" , 15) , bg  = "white" , anchor="w" ) 
	lab6.place(x=0 , y = 200 , width = 200 , height = 20)
	e6 = Entry(customer_f, bg = "#eee5de"  )
	e6.place(x=300 , y =200 , height= 20 , width = 140 )
	lab7 = Label(customer_f , text ="Number of people:        ",  font=("ALGERIAN" , 15) , bg  = "white" , anchor="w" ) 
	lab7.place(x=0 , y = 240 , width = 200 , height = 20)
	e7 = Entry(customer_f, bg = "#eee5de"  )
	e7.place(x=300 , y =240 , height= 20 , width = 140 )
	list1 =[]

	def find_table() :
		capa = e7.get() 	
		name = (capa , )
		sql = "SELECT t_id FROM dbms_project.tab_les  WHERE capacity >= %s ;"
		my_cursor.execute( sql, name)
		for x in my_cursor:
			list1.append(x)
		return list1
	list1 = find_table()
	lab8 = Label(customer_f , text  = "Table Number : " ,   font=("ALGERIAN" , 15) , bg  = "white" , anchor="w")
	lab8.place(x =0 , y= 280 , height= 20 , width= 200)
	drop = ttk.Combobox(customer_f , values =list1 )
	drop.place(x =300 , y = 280,height= 20 , width=140)
	def add_customer() :
		sql_command= "INSERT INTO customers ( c_name, c_phone, c_address, c_occupation ) VALUES ( %s ,%s , %s , %s ) "
		values  = ( e1.get() , e3.get() , e2.get() , e4.get() )
		my_cursor.execute(sql_command , values)
		mydb.commit()
		last_id = my_cursor.lastrowid
		print((last_id))
		sql_command =  "INSERT INTO booking(b_date , b_hour , c_id , t_id) VALUES ( %s , %s , %s ,%s)"
		values = (e5.get() , e6.get() ,last_id , drop.get())
		my_cursor.execute(sql_command , values)
		mydb.commit()
	button = Button(customer_f, text = "Book  " ,command= add_customer,  font=("ALGERIAN" , 15) , bg  = "red"  )
	button.place(x= 120 , y = 320 ,  width = 140 , height= 40 )

def add_food():
	
	food_f = Frame(frame1 , bg = "white")
	food_f.place(x= 152 , y = 50 , relwidth= 1 , height= 450 )
	dash_label= Label(frame1 , text = "Add Food" , font = ("times new roman",15) , justify= 'left')
	dash_label.place(x =150 , y =0  , width =800 , height= 50 )
	food1 = Label( food_f , text ="Food  Name     : "  , font=("ALGERIAN" , 15) , bg  = "white", anchor="w" ) 
	food1.place(x=150 , y = 0 , width = 200 , height = 20)
	food_e1 = Entry( food_f, bg = "#eee5de"  )
	food_e1.place(x=400 , y =0 , height= 20 , width = 140 )
	food2 = Label( food_f , text ="Food Price          :  " ,  font=("ALGERIAN" , 15) , bg = "white" ,anchor="w") 
	food2.place(x=150 , y = 40 , width = 200 , height = 20)
	food_e2 = Entry( food_f, bg = "#eee5de"  )
	food_e2.place(x=400 , y =40, height= 20 , width = 140 )
	food3 = Label( food_f , text ="Employee ID :  ",  font=("ALGERIAN" , 15) , bg = "white" , anchor="w" ) 
	food3.place(x=150 , y = 80 , width = 200 , height = 20)
	food_e3 = Entry( food_f, bg = "#eee5de"  )
	food_e3.place(x=400 , y =80, height= 20 , width = 140 )

	def show_food():
		my_cursor.execute("SELECT * FROM foods")
		result = my_cursor.fetchall()
		num  =40 
		print(result)
		for index , x in enumerate(result):
			num2 = -180
			for y in x :
				loc_lab_1 = Label(sub_frame ,  text= y  , bg = "white" )
				loc_lab_1.place(x= (num2 + 180)  , y = num , height= 30 , width = 190)
				num2 = (num2+180)
			
			num  = num + 40
	
	
	def add_food():
		sql_C = "INSERT INTO foods (f_name , f_price , e_id) VALUES(%s , %s ,%s)"
		values = (food_e1.get() , food_e2.get() , food_e3.get())
		my_cursor.execute(sql_C , values)
		mydb.commit()
		show_food()
	
	
	
	food_button = Button(food_f, text = "Book  ", command= add_food,  font=("ALGERIAN" , 15) , bg  = "red"  )
	food_button.place(x= 150 , y = 150 ,  width = 140 , height= 40 )


	sub_frame = Frame(food_f, bg = "lightgray")
	sub_frame.place(x= 0 , y = 200 , relwidth=1 , height=270 )
	

	lab_1 = Label(sub_frame , text  = "F_Id" , bg = "#eee5de")
	lab_1.place(x = 0 , y = 0 , width = 200 , height= 30)

	lab_2 = Label(sub_frame , text  = "Food Name" , bg = "#eee5de")
	lab_2.place(x = 180 , y = 0 , width = 200 , height= 30)

	lab_3 = Label(sub_frame , text  = "Food Price" , bg = "#eee5de")
	lab_3.place(x = 360 , y = 0 , width = 200 , height= 30)

	lab_4 = Label(sub_frame , text  = "Employee Id" , bg = "#eee5de")
	lab_4.place(x = 540 , y = 0 , width = 210 , height= 30)
	show_food()
	
def employee():
	Emplyoee_f = Frame(frame1 , bg = "white")
	Emplyoee_f.place(x= 152 , y = 50 , relwidth= 1 , height= 450 )
	Das_Emp_lab = Label(frame1 , bg = "#daf2f0" , text = " Add Employee Details")
	Das_Emp_lab.place(x= 0 , y =0  , height= 50  , relwidth= 1)
	Emp_lab_1 = Label(Emplyoee_f , text ="Employee Name     : "  , font=("ALGERIAN" , 15) , bg  = "white", anchor="w" ) 
	Emp_lab_1.place(x=0 , y = 10 , width = 200 , height = 20)
	Emp1 = Entry(Emplyoee_f, bg = "#daf2f0"  )
	Emp1.place(x=300 , y =10 , height= 20 , width = 140 )
	Emp_lab_2 = Label(Emplyoee_f , text ="Phone Number          :  " ,  font=("ALGERIAN" , 15) , bg = "white" ,anchor="w") 
	Emp_lab_2.place(x=0 , y = 50 , width = 200 , height = 20)
	Emp2 = Entry(Emplyoee_f, bg = "#daf2f0"  )
	Emp2.place(x=300 , y =50, height= 20 , width = 140 )
	Emp_lab_3 = Label(Emplyoee_f , text ="Employee Address  :  ",  font=("ALGERIAN" , 15) , bg = "white" , anchor="w" ) 
	Emp_lab_3.place(x=0 , y = 90 , width = 200 , height = 20)
	Emp3 = Entry(Emplyoee_f, bg = "#daf2f0"  )
	Emp3.place(x=300 , y =90, height= 20 , width = 140 )
	Emp_lab_4 = Label(Emplyoee_f, text ="Employee  salary     :  ",  font=("ALGERIAN" , 15) , bg  = "white" , anchor="w" ) 
	Emp_lab_4.place(x=0 , y = 130 , width = 200 , height = 20)
	Emp4 = Entry(Emplyoee_f, bg = "#daf2f0"  )
	Emp4.place(x=300, y =130 , height= 20 , width = 140 )

	Emp_lab_5 = Label(Emplyoee_f, text ="Job ID     :  ",  font=("ALGERIAN" , 15) , bg  = "white" , anchor="w" ) 
	Emp_lab_5.place(x=0 , y = 170 , width = 200 , height = 20)
	Emp5 = Entry(Emplyoee_f, bg = "#daf2f0"  )
	Emp5.place(x=300, y =170 , height= 20 , width = 140 )

	sub_frame = Frame(Emplyoee_f , bg = "#eee5de")
	sub_frame.place(x= 0 , y= 260 , relwidth= 1 , height= 270 )

	myscrollbar=Scrollbar(sub_frame,orient="vertical")
	myscrollbar.pack(side="left",fill="y")
	def show_employee() :
		my_cursor.execute("SELECT * FROM employees")
		result = my_cursor.fetchall()
		num  =40 
		for index , x in enumerate(result):
			num2 = -150
			for y in x :
				loc_lab_1 = Label(sub_frame ,  text= y  , bg = "white" )
				loc_lab_1.place(x= (num2 + 150)  , y = num , height= 30 , width = 170)
				num2 = (num2+150)
				
			num  = num + 40

	lab_1 = Label(sub_frame , text  = "Employee ID" , bg = "#eee5de")
	lab_1.place(x = 0 , y = 0 , width = 170 , height= 30)

	lab_2 = Label(sub_frame , text  = "Employee Name" , bg = "#eee5de")
	lab_2.place(x = 150 , y = 0 , width = 170 , height= 30)

	lab_3 = Label(sub_frame , text  = "Phone Number" , bg = "#eee5de")
	lab_3.place(x = 300 , y = 0 , width = 170 , height= 30)

	lab_4 = Label(sub_frame , text  = "Address" , bg = "#eee5de")
	lab_4.place(x = 450 , y = 0 , width = 170 , height= 30)

	lab_5 = Label(sub_frame , text  = "Salary" , bg = "#eee5de")
	lab_5.place(x = 600 , y = 0 , width = 170 , height= 30)

	show_employee()


#lace(x= 500  , y = 10 , height=200 , width= 200)
	#main frame
	sub_f = Frame(Emplyoee_f , bg = "#eee5de")
	sub_f.place(x= 500  , y = 10 , height=200 , width= 200)
	#canvas frame
	


	sql_sub = "SELECT * FROM jobs"
	my_cursor.execute(sql_sub)
	result=  my_cursor.fetchall()
	labe_sub = Label(sub_f, text = "J_id", bg = "#daf2f0")
	labe_sub.place(x= 0 , y = 0 , width= "100" , height= 30)
	labe_sub_2 = Label(sub_f , text = "Title" , bg = "#daf2f0")
	labe_sub_2.place(x= 100, y= 0 , width= 100 , height= 30)
	num =40
	for index , x in enumerate(result):
			num2 =-50
			for y in x :
				loc_lab_1 = Label(sub_f ,  text= y  , bg = "white" )
				loc_lab_1.place(x= (num2 + 50)  , y = num , height= 30 , width =100 )
				num2 = (num2+100)
			num = num+40



	def add_employee():
		sql = "INSERT INTO employees (e_name , e_phone , e_address , e_salary , j_id)  VALUES (%s , %s ,%s ,%s , %s)"
		values = (Emp1.get() , Emp2.get() , Emp3.get() , Emp4.get() , Emp5.get())
		my_cursor.execute(sql , values)
		mydb.commit()
	Emp_button = Button(Emplyoee_f , text = "Add Data" ,bg = "#daf2f0" , command= add_employee )
	Emp_button.place(x = 180  , y = 210 , width= 150 , height= 40)

	














































if __name__ == "__main__":
	# create_table_jobs()
	# create_table_employees()
	# jobs_description()
	# employees_description()
	# create_table_tables()
	# tables_description()
	# create_table_food()
	# foods_description()
	# create_table_customers()*
	# cutomers_description()
	# create_table_orders()
	# orders_description()
	# create_table_order_history()
	# order_history_description()
	# create_table_items()
	# items_description()
	# create_table_booking()
	# booking_description()
	# view_databases()
	root = Tk()
	root.title("DBMS PROJECT")
	root.geometry("1200x800+160+0")
	root.config(bg= "white")
	bg = ImageTk.PhotoImage(file ="E:/TY/Dbms/project/main-image.jpg")
	bg1 = Label(root , image=bg).place(x=0,y=0 , relwidth=1 , relheight=1)
	# next_image = ImageTk.PhotoImage(file="E:/TY/Dbms/project/button_2.png")
	# next_button = Button(root, text ="Next" , image= next_image , border =0  )
	# next_button.place(x=1000 ,y= 690,width=150 ,height=70 )
	
	frame1 = Frame(root , bg = "white")
	frame1.place(x= 155 , y = 170 , width= 900 , height= 500) 
	# side_image = ImageTk.PhotoImage(file="side_image_2.jpg")
	# side_image1 = Label(root , image = side_image).place(x= 90  , y = 300 , width = 220 , height= 220)
	# frame_image = ImageTk.PhotoImage(file= "frame_image1.jpg")
	# frame_image1= Label(frame1, image = frame_image).place(x= 0, y =0  , relheight= 1 , relwidth= 1)


	#frame 1 dashboard
	
	frame2 = Frame(frame1 , bg="#debba1")
	frame2.place(x=0 , y=0 , width=150 , relheight=1)



	# frame3 = Frame(frame1 , bg="pink")
	# frame3.place(x=850 , y=0 , width=50 , relheight=1)
	label_mein = Label(frame2 , text = "Main" , bg = "#debba1" ,  font=("ALGERIAN", 22))
	label_mein.place(x= 0 , y  = 50, height  = 50 , width = 150 )

	customer_button = Button(frame2 , text  = "Customer" , command= lambda : customer(frame1), bg = "#debba1" ,  font=("ALGERIAN", 18  ) , border= 0)
	customer_button.place(x= 10 , y =100 , height=40 , width= 120)


	addfood_button = Button(frame2 , text = "Add Food",  command= add_food ,bg = "#debba1" ,  font=("ALGERIAN", 18), border= 0)
	addfood_button.place(x= 10 , y =200 , height=40 , width= 120)


	employes_button = Button(frame2  , text = "Employee", command = employee ,bg = "#debba1", font=("ALGERIAN", 18)  , border= 0)
	employes_button.place(x= 10 , y =300 , height=40 , width= 120)
	order_button = Button(frame2 , bg = "#debba1"  , text ="order" , border=0 ,  font=("ALGERIAN", 18) )
	order_button.place(x= 10 , y =400 , height=40 , width= 120)

	# dashboard bar :

	frame4 = Frame (frame1  ,bg = "#daf2f0")
	frame4.place(x=0 , y =0  , width =900 , height = 50 )




	#buttons to all frames 
	# customer_button = Button(frame1 , text  = "Customer" , bg = "lightblue")
	# customer_button.place(x= 100 , y =100 , height=50 , width= 150)
	# addfood_button = Button(frame1 , text = "Add Food", bg = "lightblue")
	# addfood_button.place(x= 100 , y =200 , height=50 , width= 150)
	# employes_button = Button(frame1  , text = "Employee", bg = "lightblue")
	# employes_button.place(x= 300 , y =100 , height=50 , width= 150)
	# order_button = Button(frame1 , bg = "lightblue")
	# order_button.place(x= 300 , y =200 , height=50 , width= 150)
	root.mainloop()
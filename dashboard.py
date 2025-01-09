import tkinter as tk  # Import tkinter with an alias
from tkinter import PhotoImage, Button, Frame, Label, Entry, Scrollbar
from datetime import datetime
from tkinter import ttk
from tkinter.constants import HORIZONTAL, VERTICAL, BOTTOM, RIGHT
#from tkinter import d
from tkcalendar import dateentry, DateEntry


#functionality

def employee_form():

    global back_arrow
    employee_frame=Frame(window, width=1080, height=567, bg='white')
    employee_frame.place(x=250,y=100, )
    employee_label=Label(employee_frame, text='Manage Employee Details', font=('arial', 20, 'bold'), fg='white', background='purple')
    employee_label.place(x=0,y=0,relwidth=1)
    back_arrow=PhotoImage(file='left-arrow.png')
    back_button=Button(employee_frame, image=back_arrow,bg='white', bd=0, cursor='hand2', command=lambda : employee_frame.place_forget())
    back_button.place(x=10,y=40)

    topFrame=Frame(employee_frame, bg='white')
    topFrame.place(x=0, y=70, relwidth=1, height=235)

    search_frame=Frame(topFrame, bg='white')
    search_frame.pack()

    search_combobox=ttk.Combobox(search_frame,values=('Id', 'Name', 'Email', 'Cell'), state='readonly')
    search_combobox.set('Search By')
    search_combobox.grid(row=0, column=0, padx=20)

    search_entry=Entry(search_frame, bg='light yellow')
    search_entry.grid(row=0, column=1)

    search_button=Button(search_frame, text='Search', width=10)
    search_button.grid(row=0,column=3, padx=20 )

    show_button=Button(search_frame, text='Show All', width=10)
    show_button.grid(row=0,column=4)



    horizontal_scrollbar=Scrollbar(topFrame, orient=HORIZONTAL)
    vertical_scrollbar=Scrollbar(topFrame, orient=VERTICAL)

    employee_treeview=ttk.Treeview(topFrame, columns=('Id', 'Name', 'Email', 'gender', 'dob', "contact", 'employement_type','education','work_shift','address','doj','salary', 'usertype' ), show='headings',
                                   yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)

    horizontal_scrollbar = tk.Scrollbar(topFrame, orient=tk.HORIZONTAL)
    horizontal_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    vertical_scrollbar = tk.Scrollbar(topFrame, orient=tk.VERTICAL)
    vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


    employee_treeview.pack(pady=10)

    employee_treeview.heading('Id',text='EmpID')
    employee_treeview.heading('Name',text='Name')
    employee_treeview.heading('Email', text='Email')
    employee_treeview.heading('gender', text='Gender')
    employee_treeview.heading('dob', text='DOB')
    employee_treeview.heading('contact', text='Contact')
    employee_treeview.heading('employement_type', text='Employment_Type')
    employee_treeview.heading('education', text='Education')
    employee_treeview.heading('work_shift',text='Work Shift')
    employee_treeview.heading('address', text='Address')
    employee_treeview.heading('doj', text='DOJ')
    employee_treeview.heading('salary', text='Salary')
    employee_treeview.heading('usertype', text='User Type')

    employee_treeview.column('Id', width=60)
    employee_treeview.column('Name', width=160)
    employee_treeview.column('Email', width=160)
    employee_treeview.column('gender', width=80)
    employee_treeview.column('dob', width=100)
    employee_treeview.column('contact', width=100)
    employee_treeview.column('employement_type', width=100)
    employee_treeview.column('education', width=100)
    employee_treeview.column('work_shift', width=100)
    employee_treeview.column('address', width=200)
    employee_treeview.column('doj', width=100)
    employee_treeview.column('salary', width=100)
    employee_treeview.column('usertype', width=100)


    detail_frame=Frame(employee_frame)
    detail_frame.place(x=0, y=300)

    empid_lable=Label(detail_frame, text='EmpID')
    empid_lable.grid(row=0, column=0)
    empid_entry=Entry(detail_frame, bg='light yellow')
    empid_entry.grid(row=0, column=1, padx=20, pady=10)

    name_lable = Label(detail_frame, text='Name')
    name_lable.grid(row=0, column=2)
    name_entry = Entry(detail_frame, bg='light yellow')
    name_entry.grid(row=0, column=3, padx=20, pady=10)

    Email_lable = Label(detail_frame, text='Email')
    Email_lable.grid(row=0, column=4)
    Email_entry = Entry(detail_frame, bg='light yellow')
    Email_entry.grid(row=0, column=5, padx=20, pady=10)

    gender_lable = Label(detail_frame, text='Gender')
    gender_lable.grid(row=1, column=0)
    gender_combobox=ttk.Combobox(detail_frame, values=('Male', 'Female'), width=18, state='readonly')
    gender_combobox.grid(row=1, column=1)

    dob_lable = Label(detail_frame, text='Date of Birth')
    dob_lable.grid(row=1, column=2)
    dob_combobox = DateEntry(detail_frame,  width=18, state='readonly', date_pattern='dd/mm/yyyy')
    dob_combobox.grid(row=1, column=3)








# Create the main window
window = tk.Tk()
window.title("Dashboard")  # Set the title of the window
window.geometry("1270x680+0+0")  # Set the window size

bg_image=PhotoImage(file="inventry.png")
# Create and display a label
titleLabel = tk.Label(window, image=bg_image,compound="left", text="        Inventory Management System", font=("Arial", 20, 'bold'), bg="lightblue", fg="black", anchor="w", padx=20)
titleLabel.place(x=0,y=0, relwidth=1 )
logoutButton=Button(window,text="Logout", font=("Arial", 10, 'bold'))
logoutButton.place(x=1100,y=10)
current_datetime=datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
subtitleLabel = tk.Label(text="welcom Admin\t\t {formatted_datetime}" ,  font=("Arial", 20, 'bold'))
subtitleLabel.place(x=0,y=70, relwidth=1 )

leftFrame=Frame(window)
leftFrame.place(x=0,y=102, width= 250, height= 600)
logoimage=PhotoImage(file='img1.png')
imageLabel=Label(leftFrame,image=logoimage)
imageLabel.pack(fill='x')

menuLabel=Label(leftFrame, text="Menu", font=("Arial", 20, 'bold'),bg="lightblue", fg="black")
menuLabel.pack(fill='x')

employee_icon=PhotoImage(file='owner.png')
emplyee_Button=Button(leftFrame, image=employee_icon, compound="left",text="  Employees", font=('Arial', 20, 'bold'),anchor='w', padx=10, command=employee_form)
emplyee_Button.pack(fill='x')

suplier_icon=PhotoImage(file='tracking.png')
supplier_Button=Button(leftFrame, image=suplier_icon, compound='left', text=' Supplier', font=('Arial', 20, 'bold'),anchor='w', padx=10)
supplier_Button.pack(fill='x')

cat_icon=PhotoImage(file='categorization.png')
cat_Button=Button(leftFrame, image=cat_icon, compound='left', text='  Categories', font=('arial', 20, 'bold'),anchor='w', padx=10)
cat_Button.pack(fill='x')

product_icon=PhotoImage(file='products.png')
product_Button=Button(leftFrame, image=product_icon, compound='left', text='  Products', font=('arial',20,'bold'),anchor='w', padx=10)
product_Button.pack(fill='x')

sale_icon=PhotoImage(file='trend.png')
sale_Button=Button(leftFrame, image=sale_icon, compound='left', text='  Sales', font=('arial', 20, 'bold'),anchor='w', padx=10)
sale_Button.pack(fill='x')

exit_icon=PhotoImage(file='logout.png')
exit_Button=Button(leftFrame, image=exit_icon,compound='left', text='  Exit', font=('arial', 20, 'bold'),anchor='w', padx=10)
exit_Button.pack(fill='x')

emp_frame=Frame(window, bg='blue')
emp_frame.place(x=400,y=130, height=100, width=280)

emp_frame_label=Label(emp_frame, text='Total Employees', font=('arial',15,'bold'), fg='white', bg='blue')
emp_frame_label.pack()

emp_frame_count_label=Label(emp_frame, text='0', font=('arial',30,'bold'), fg='white', bg='blue')
emp_frame_count_label.pack()

suplier_frame=Frame(window, bg='blue')
suplier_frame.place(x=800,y=130, height=100, width=280)

suplier_frame_label=Label(suplier_frame, text='Total supplier', font=('arial',15,'bold'), fg='white', bg='blue')
suplier_frame_label.pack()

suplier_frame_count_label=Label(suplier_frame, text='0', font=('arial',30,'bold'), fg='white', bg='blue')
suplier_frame_count_label.pack()

cat_frame=Frame(window, bg='blue')
cat_frame.place(x=400,y=280, height=100, width=280)

cat_frame_label=Label(cat_frame, text='Total categories', font=('arial',15,'bold'), fg='white', bg='blue')
cat_frame_label.pack()

cat_frame_count_label=Label(cat_frame, text='0', font=('arial',30,'bold'), fg='white', bg='blue')
cat_frame_count_label.pack()

product_frame=Frame(window, bg='blue')
product_frame.place(x=800,y=280, height=100, width=280)

product_frame_label=Label(product_frame, text='Total products', font=('arial',15,'bold'), fg='white', bg='blue')
product_frame_label.pack()

product_frame_count_label=Label(product_frame, text='0', font=('arial',30,'bold'), fg='white', bg='blue')
product_frame_count_label.pack()

sale_frame=Frame(window, bg='blue')
sale_frame.place(x=600,y=420, height=100, width=280)

sale_frame_label=Label(sale_frame, text='Total sale', font=('arial',15,'bold'), fg='white', bg='blue')
sale_frame_label.pack()

sale_frame_count_label=Label(sale_frame, text='0', font=('arial',30,'bold'), fg='white', bg='blue')
sale_frame_count_label.pack()

# Run the Tkinter main loop
window.mainloop()

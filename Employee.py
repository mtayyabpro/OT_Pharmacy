from tkinter import *
from tkinter import ttk

import pymysql
from tkcalendar import DateEntry
import tkinter as tk
from tkinter import messagebox


def connect_database():
    try:
        conntection = pymysql.connect(host='localhost', user='root', password='admin')
        mycursor = conntection.cursor()
    except:
        messagebox.showerror('error', 'Database connectivity issue try again, open mysql command line')
        return
    #mycursor.execute('CREATE DATABASE IF NOT EXIST OT_Pharmacy')
    mycursor.execute('USE ortho')
    #mycursor.execute('CREATE TABLE IF NOT EXIST employee_data')

    connect_database()


def employee_form(window):
    global back_arrow
    employee_frame = Frame(window, width=1080, height=567, bg='white')
    employee_frame.place(x=250, y=100, )
    employee_label = Label(employee_frame, text='Manage Employee Details', font=('arial', 20, 'bold'), fg='white',
                           background='purple')
    employee_label.place(x=0, y=0, relwidth=1)
    back_arrow = PhotoImage(file='left-arrow.png')
    back_button = Button(employee_frame, image=back_arrow, bg='white', bd=0, cursor='hand2',
                         command=lambda: employee_frame.place_forget())
    back_button.place(x=10, y=40)

    topFrame = Frame(employee_frame, bg='white')
    topFrame.place(x=0, y=70, relwidth=1, height=235)

    search_frame = Frame(topFrame, bg='white')
    search_frame.pack()

    search_combobox = ttk.Combobox(search_frame, values=('Id', 'Name', 'Email', 'Cell'), state='readonly')
    search_combobox.set('Search By')
    search_combobox.grid(row=0, column=0, padx=20)

    search_entry = Entry(search_frame, bg='light yellow')
    search_entry.grid(row=0, column=1)

    search_button = Button(search_frame, text='Search', width=10)
    search_button.grid(row=0, column=3, padx=20)

    show_button = Button(search_frame, text='Show All', width=10)
    show_button.grid(row=0, column=4)

    horizontal_scrollbar = Scrollbar(topFrame, orient=HORIZONTAL)
    vertical_scrollbar = Scrollbar(topFrame, orient=VERTICAL)

    employee_treeview = ttk.Treeview(topFrame, columns=(
    'Id', 'Name', 'Email', 'gender', 'dob', "contact", 'employement_type', 'education', 'work_shift', 'address', 'doj',
    'salary', 'usertype'), show='headings',
                                     yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)

    horizontal_scrollbar = tk.Scrollbar(topFrame, orient=tk.HORIZONTAL)
    horizontal_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    vertical_scrollbar = tk.Scrollbar(topFrame, orient=tk.VERTICAL)
    vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    employee_treeview.pack(pady=10)

    employee_treeview.heading('Id', text='EmpID')
    employee_treeview.heading('Name', text='Name')
    employee_treeview.heading('Email', text='Email')
    employee_treeview.heading('gender', text='Gender')
    employee_treeview.heading('dob', text='DOB')
    employee_treeview.heading('contact', text='Contact')
    employee_treeview.heading('employement_type', text='Employment_Type')
    employee_treeview.heading('education', text='Education')
    employee_treeview.heading('work_shift', text='Work Shift')
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

    detail_frame = Frame(employee_frame)
    detail_frame.place(x=20, y=300)

    empid_lable = Label(detail_frame, text='EmpID')
    empid_lable.grid(row=0, column=0)
    empid_entry = Entry(detail_frame, bg='light yellow')
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
    gender_combobox = ttk.Combobox(detail_frame, values=('Male', 'Female'), width=18, state='readonly')
    gender_combobox.set('select gender')
    gender_combobox.grid(row=1, column=1)

    dob_lable = Label(detail_frame, text='Date of Birth')
    dob_lable.grid(row=1, column=2)
    dob_lable = DateEntry(detail_frame, width=18, state='readonly', date_pattern='dd/mm/yyyy')
    dob_lable.grid(row=1, column=3)

    contact_lable = Label(detail_frame, text='Contact')
    contact_lable.grid(row=1, column=4)
    contact_lable = Entry(detail_frame, bg='light yellow')
    contact_lable.grid(row=1, column=5, padx=20, pady=10)

    emp_type_lable = Label(detail_frame, text='Employee Type')
    emp_type_lable.grid(row=2, column=0)
    emp_type_combobox = ttk.Combobox(detail_frame, values=('Regular', 'Contract', 'Adhoc'), width=18, state='readonly')
    emp_type_combobox.set('select type')
    emp_type_combobox.grid(row=2, column=1, padx=20, pady=10)

    emp_edu_lable = Label(detail_frame, text='Education')
    emp_edu_lable.grid(row=2, column=2)
    emp_edu_combobox = ttk.Combobox(detail_frame, values=('Regular', 'Contract', 'Adhoc'), width=18, state='readonly')
    emp_edu_combobox.set('select Education')
    emp_edu_combobox.grid(row=2, column=3, padx=20, pady=10)

    emp_shift_lable = Label(detail_frame, text='Employee Shift')
    emp_shift_lable.grid(row=2, column=4, padx=20, pady=10)
    emp_shift_combobox = ttk.Combobox(detail_frame, values=('Morning', 'Evening', 'night'), width=18, state='readonly')
    emp_shift_combobox.set('select Shift')
    emp_shift_combobox.grid(row=2, column=5)

    add_lable = tk.Label(detail_frame, text='address')
    add_lable.grid(row=3, column=0, padx=20, pady=10)

    add_text = tk.Text(detail_frame, width=18, height=3, bg='light yellow')
    add_text.grid(row=3, column=1, rowspan=2)

    doj_lable = Label(detail_frame, text='Date of Joining')
    doj_lable.grid(row=3, column=2)
    doj_lable = DateEntry(detail_frame, width=18, state='readonly', date_pattern='dd/mm/yyyy')
    doj_lable.grid(row=3, column=3)

    salary_lable = Label(detail_frame, text='Salary')
    salary_lable.grid(row=3, column=4)
    salary_lable = Entry(detail_frame, bg='light yellow')
    salary_lable.grid(row=3, column=5, padx=20, pady=10)

    user_type_lable = Label(detail_frame, text='User Type')
    user_type_lable.grid(row=4, column=2, padx=20, pady=10)
    user_type_combobox = ttk.Combobox(detail_frame, values=('Admin', 'Evening', 'night'), width=18, state='readonly')
    user_type_combobox.set('select User Type')
    user_type_combobox.grid(row=4, column=3)

    password_lable = Label(detail_frame, text='Password')
    password_lable.grid(row=4, column=4)
    password_lable = Entry(detail_frame, bg='light yellow')
    password_lable.grid(row=4, column=5, padx=20, pady=10)

    button_frame = Frame(employee_frame)
    button_frame.place(x=200, y=500)
    add_button = Button(button_frame, text='Add', width=10)
    add_button.grid(row=0, column=2, padx=20)

    clear_button = Button(button_frame, text='clear', width=10)
    clear_button.grid(row=0, column=3, padx=20)

    update_button = Button(button_frame, text='Update', width=10)
    update_button.grid(row=0, column=4, padx=20)

    delete_button = Button(button_frame, text='Delete', width=10)
    delete_button.grid(row=0, column=5, padx=20)

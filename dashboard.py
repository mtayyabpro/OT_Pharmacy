import tkinter as tk  # Import tkinter with an alias
from tkinter import PhotoImage, Button, Frame, Label, Entry, Scrollbar
from datetime import datetime

from Employee import employee_form


#functionality




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
formatted_datetime = current_datetime.strftime("%d-%m-%y %H:%M:%S")
subtitleLabel = tk.Label(window,
    text=f"Welcome Admin\t\t {formatted_datetime}",  # Use f-string to include the variable
    font=("Arial", 20, "bold"))
subtitleLabel.place(x=0,y=70, relwidth=1 )

leftFrame=Frame(window)
leftFrame.place(x=0,y=102, width= 250, height= 600)
logoimage=PhotoImage(file='img1.png')
imageLabel=Label(leftFrame,image=logoimage)
imageLabel.pack(fill='x')

menuLabel=Label(leftFrame, text="Menu", font=("Arial", 20, 'bold'),bg="lightblue", fg="black")
menuLabel.pack(fill='x')

employee_icon=PhotoImage(file='owner.png')
emplyee_Button=Button(leftFrame, image=employee_icon, compound="left",text="  Employees", font=('Arial', 20, 'bold'),anchor='w', padx=10, command=lambda :employee_form(window))
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

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3


# showing the database
def query():
    conn = sqlite3.connect('yt_database.db')

    c = conn.cursor()

    # query the db
    c.execute("SELECT oid "
              "|| \". First Name: \" || first_name "
              "|| \", Last Name: \"  || last_name "
              "|| \", Age: \" || age "
              "|| \", City: \" || city "
              "|| \", Email: \" || email "
              "FROM users")
    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    print_records.translate({ord("\'"): None})
    print_records.translate({ord(")"): None})
    print_records.translate({ord("("): None})

    query_lbl = Label(second_frame)
    query_lbl.grid(row=11, column=0, columnspan=3)

    texts = Text(query_lbl)
    texts.grid(row=11, column=0, ipady=20)

    scrollbar = Scrollbar(query_lbl, command=texts.yview)
    texts.config(yscrollcommand=scrollbar.set)

    scrollbar.grid(row=11, column=3, sticky=NSEW)
    texts.insert(END, print_records)

    conn.commit()

    conn.close()


# similar to INSERT
def submit():
    conn = sqlite3.connect('yt_database.db')

    c = conn.cursor()

    # insert into table
    c.execute("INSERT INTO users(first_name, last_name, age, city, email, role_type) VALUES (:first_name, :last_name, "
              ":age,:city, :email, :role_type)",
              {
                  'first_name': f_name.get(),
                  'last_name': f_lname.get(),
                  'age': age.get(),
                  'city': city.get(),
                  'email': email.get(),
                  'role_type': 'user'
              })
    c.execute("INSERT INTO login_account(username, user_password) VALUES (:username, :user_password)",
              {
                  'username': f_name.get(),
                  'user_password': password.get()
              })

    # clear the txt boxes
    f_name.delete(0, END)
    f_lname.delete(0, END)
    age.delete(0, END)
    city.delete(0, END)
    email.delete(0, END)
    password.delete(0, END)

    messagebox.showinfo("Info", "Successfully inserted!")

    conn.commit()

    conn.close()


# for the submit form
def openWinLogin():
    # connect to db
    conn = sqlite3.connect('yt_database.db')

    # create cursor instance
    c = conn.cursor()

    # commit changes
    conn.commit()

    global top, f_name, f_lname, age, city, email, password, second_frame

    # startup thingz
    top = Toplevel()
    top.resizable(0, 0)
    top.geometry("750x800")
    top.title('YouTube database')
    top.iconbitmap('Images/ytDatabaseIcon.ico')

    # center
    width = 750
    height = 800

    scr_width = top.winfo_screenwidth()
    scr_height = top.winfo_screenheight()

    x = (scr_width / 2) - (width / 2)
    y = (scr_height / 2) - (height / 2)

    top.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    # create a main frame
    main_frame = Frame(top)
    main_frame.pack(fill=BOTH, expand=1)

    # create a canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # add a scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # create another frame inside the canvas
    second_frame = Frame(my_canvas)

    # add that New frame To a Window In The Canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # create text boxes
    f_name = Entry(second_frame, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=10)

    f_lname = Entry(second_frame, width=30)
    f_lname.grid(row=1, column=1, padx=20, pady=10)

    age = Entry(second_frame, width=30)
    age.grid(row=2, column=1, padx=20, pady=10)

    city = Entry(second_frame, width=30)
    city.grid(row=3, column=1, padx=20, pady=10)

    email = Entry(second_frame, width=30)
    email.grid(row=4, column=1, padx=20, pady=10)

    password = Entry(second_frame, width=30)
    password.grid(row=5, column=1, padx=20, pady=10)

    # create text boxes labels
    f_name_label = Label(second_frame, text="First name")
    f_name_label.grid(row=0, column=0, padx=20)

    f_lname_label = Label(second_frame, text="Last name")
    f_lname_label.grid(row=1, column=0, padx=20)

    age_label = Label(second_frame, text="Age")
    age_label.grid(row=2, column=0, padx=20)

    city_label = Label(second_frame, text="City")
    city_label.grid(row=3, column=0, padx=20)

    email_label = Label(second_frame, text="Email")
    email_label.grid(row=4, column=0, padx=20)

    pass_label = Label(second_frame, text="Password")
    pass_label.grid(row=5, column=0, padx=20)

    # create submit button
    try:
        submit_btn = Button(second_frame, text="Add record", command=submit)
        submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10)
    except sqlite3.IntegrityError as e:
        tkinter.messagebox.showerror("Invalid options", "You did not insert a valid option!")

    # create close button
    go_back_btn = Button(second_frame, text="Go Back", command=top.destroy)
    go_back_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

    # CREATE A QUERY BUTTON
    query_btn = Button(second_frame, text="Show Records", command=query)
    query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    conn.commit()
    conn.close()

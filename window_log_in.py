import tkinter
from tkinter import *
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


def insertDB():
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


def updateDB():
    pass


def deleteDB():
    pass


# for the menu form
def openWinDb():
    # connect to db
    conn = sqlite3.connect('yt_database.db')

    # create cursor instance
    c = conn.cursor()

    top = Toplevel()
    top.resizable(0, 0)
    top.geometry("500x400")
    top.title('YouTube database')
    top.iconbitmap('Images/ytDatabaseIcon.ico')

    frame = Frame(top)
    frame.pack()

    # create a menu
    my_menu = Menu(frame)
    frame.config(menu=my_menu)

    # commit changes
    conn.commit()

    conn.close()

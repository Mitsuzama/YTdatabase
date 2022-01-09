import tkinter
from tkinter import *
import sqlite3
import GUI.modify as m
import GUI.deleteFile as d
import GUI.updateFile as u


# done
# showing the database
def query(table_name):
    conn = sqlite3.connect('yt_database.db')

    c = conn.cursor()

    table_name = str(table_name).lower()

    if table_name == "users":

        c.execute("SELECT oid "
                  "|| \". First Name: \" || first_name "
                  "|| \", Last Name: \"  || last_name "
                  "|| \", Age: \" || age "
                  "|| \", City: \" || city "
                  "|| \", Email: \" || email "
                  "FROM users")

    elif table_name == "roles":

        c.execute("SELECT oid "
                  "|| \". Role Type: \" || role_type "
                  "FROM roles")
        records = c.fetchall()

    elif table_name == "videos":
        c.execute("SELECT oid "
                  "|| \". Title: \" || title "
                  "|| \", Person who posted: \"  || user_id "
                  "|| \", Number of likes: \" || no_of_likes "
                  "FROM videos")

    elif table_name == "video_comment":
        c.execute("SELECT oid "
                  "|| \". User who posted: \" || user_id "
                  "|| \", Video: \"  || video_id "
                  "|| \", The comment: \" || comments "
                  "FROM video_comment")

    elif table_name == "login_account":
        c.execute("SELECT oid "
                  "|| \". Username: \" || username "
                  "|| \", User password: \"  || user_password "
                  "FROM login_account")

    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_lbl = Label(bottom_frame)
    query_lbl.grid(row=0, column=3, columnspan=3)

    texts = Text(query_lbl)
    texts.grid(row=0, column=4, ipady=20)

    scrollbar = Scrollbar(query_lbl, command=texts.yview)
    texts.config(yscrollcommand=scrollbar.set)

    scrollbar.grid(row=0, column=5, sticky=NSEW)
    texts.insert(END, print_records)

    conn.commit()

    conn.close()

def updatebtndef(ala):
    if ala == "Users":
        u.users_update()
    elif ala == "Videos":
        u.videos_update()
    elif ala == "Video_Comment":
        u.video_comment_update()
    elif ala == "Login_Account":
        u.login_update()

# DONE
def deletebtndef(ala):
    if ala == "Users":
        d.users_delete()
    elif ala == "Videos":
        d.videos_delete()
    elif ala == "Video_Comment":
        d.video_comment_delete()
    elif ala == "Login_Account":
        d.login_delete()


# DONE
def modifybtndef(ala):
    if ala == "Users":
        m.users_insert()
    elif ala == "Videos":
        m.videos_insert()
    elif ala == "Video_Comment":
        m.video_comment_insert()
    elif ala == "Login_Account":
        m.login_insert()


# DONE
def insertDB():
    conn = sqlite3.connect('yt_database.db')

    c = conn.cursor()

    tables_label = Label(up_frame, text="Choose table to modify")
    tables_label.grid(row=0, column=0, columnspan=2)

    table_listbox = Listbox(up_frame)

    table_listbox.insert(1, "Users")
    table_listbox.insert(2, "Videos")
    table_listbox.insert(3, "Video_Comment")
    table_listbox.insert(4, "Login_Account")
    table_listbox.grid(row=1, column=0, columnspan=2)

    modify_btn = Button(up_frame, text="Modify", command=lambda: modifybtndef(table_listbox.get(ANCHOR)))
    modify_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    conn.commit()

    conn.close()


def updateDB():
    conn = sqlite3.connect('yt_database.db')

    c = conn.cursor()

    tables_label = Label(up_frame, text="Choose table to modify")
    tables_label.grid(row=0, column=0, columnspan=2)

    table_listbox = Listbox(up_frame)

    table_listbox.insert(1, "Users")
    table_listbox.insert(2, "Videos")
    table_listbox.insert(3, "Video_Comment")
    table_listbox.insert(4, "Login_Account")
    table_listbox.grid(row=1, column=0, columnspan=2)

    modify_btn = Button(up_frame, text="Modify", command=lambda: updatebtndef(table_listbox.get(ANCHOR)))
    modify_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    conn.commit()

    conn.close()

    conn.close()


def deleteDB():
    conn = sqlite3.connect('yt_database.db')

    c = conn.cursor()

    tables_label = Label(up_frame, text="Choose table to modify")
    tables_label.grid(row=0, column=0, columnspan=2)

    table_listbox = Listbox(up_frame)

    table_listbox.insert(1, "Users")
    table_listbox.insert(2, "Videos")
    table_listbox.insert(3, "Video_Comment")
    table_listbox.insert(4, "Login_Account")
    table_listbox.grid(row=1, column=0, columnspan=2)

    modify_btn = Button(up_frame, text="Modify", command=lambda: deletebtndef(table_listbox.get(ANCHOR)))
    modify_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    conn.commit()

    conn.close()

    conn.close()


# for the menu form
def openWinDb():
    # connect to db
    conn = sqlite3.connect('yt_database.db')

    # create cursor instance
    c = conn.cursor()

    global bottom_frame, up_frame

    top1 = Toplevel()
    top1.title('YouTube database')
    top1.iconbitmap('Images/ytDatabaseIcon.ico')

    width = 1200
    height = 700

    screen_width = top1.winfo_screenwidth()
    screen_height = top1.winfo_screenheight()

    top1.geometry(f'{screen_width}x{screen_height}')

    # upside frame initialisation
    up_frame = LabelFrame(top1, text='Modify')
    up_frame.grid(column=0, row=0, padx=20, pady=20)

    # create a menu
    my_menu = Menu(up_frame)
    my_menu.add_command(label="Insert", command=insertDB)
    my_menu.add_command(label="Update", command=updateDB)
    my_menu.add_command(label="Delete", command=deleteDB)
    my_menu.add_command(label="Exit", command=top1.destroy)

    top1.config(menu=my_menu)

    # bottom frame configure
    bottom_frame = LabelFrame(top1, text='Show')
    bottom_frame.grid(column=0, row=1, padx=20, pady=20, columnspan=2)
    bottom_frame.grid_rowconfigure(1, weight=1)

    tables_label = Label(bottom_frame, text="Choose the table you want to see")
    tables_label.grid(row=0, column=0, ipadx=10, ipady=10)

    table_listbox = Listbox(bottom_frame)

    table_listbox.insert(1, "Roles")
    table_listbox.insert(2, "Users")
    table_listbox.insert(3, "Videos")
    table_listbox.insert(4, "Video_Comment")
    table_listbox.insert(5, "Login_Account")
    table_listbox.grid(row=1, column=0, ipadx=10, ipady=10)

    # query button
    show_recs = Button(bottom_frame, text="Show Records", command=lambda: query(table_listbox.get(ANCHOR)))
    show_recs.grid(row=2, column=0, sticky='ew', pady=10, padx=10)

    # commit changes
    conn.commit()

    conn.close()

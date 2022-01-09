import tkinter
from tkinter import *
import sqlite3
import GUI.window_log_in as wli


def u_update():
    # Create a database or connect to one
    conn = sqlite3.connect('yt_database.db')
    # Create cursor
    c = conn.cursor()

    record_id = ud_user_id.get()

    c.execute("""UPDATE users SET
            first_name = :first,
            last_name = :last,
            age = :address,
            city = :city,
            email = :email
            WHERE user_id = :oid""",
              {
                  'first': f_name_editor.get(),
                  'last': f_lname_editor.get(),
                  'address': age_editor.get(),
                  'city': city_editor.get(),
                  'email': email_editor.get(),
                  'oid': record_id
              })

    c.execute("""UPDATE login_account SET
                username = :username,
                user_password = :password
                WHERE user_id = :oid""",
              {
                  'username': f_name_editor.get(),
                  'password': password_editor.get(),
                  'oid': record_id
              })

    conn.commit()

    conn.close()

    editor.destroy()


def users_update_submit():
    global editor
    editor = Toplevel()
    editor.title('Update database')
    editor.iconbitmap('Images/ytDatabaseIcon.ico')
    editor.geometry("400x300")

    # Create a database or connect to one
    conn = sqlite3.connect('yt_database.db')
    # Create cursor
    c = conn.cursor()

    record_id = ud_user_id.get()

    # Query the database
    c.execute("SELECT * FROM users WHERE user_id = " + record_id)
    records = c.fetchall()

    # Create Global Variables for text box names
    global f_name_editor
    global f_lname_editor
    global age_editor
    global city_editor
    global email_editor
    global password_editor

    # create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=10)

    f_lname_editor = Entry(editor, width=30)
    f_lname_editor.grid(row=1, column=1, padx=20, pady=10)

    age_editor = Entry(editor, width=30)
    age_editor.grid(row=2, column=1, padx=20, pady=10)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20, pady=10)

    email_editor = Entry(editor, width=30)
    email_editor.grid(row=4, column=1, padx=20, pady=10)

    password_editor = Entry(editor, width=30)
    password_editor.grid(row=5, column=1, padx=20, pady=10)

    # create text boxes labels
    f_name_label_editor = Label(editor, text="First name")
    f_name_label_editor.grid(row=0, column=0, padx=20)

    f_lname_label_editor = Label(editor, text="Last name")
    f_lname_label_editor.grid(row=1, column=0, padx=20)

    age_label_editor = Label(editor, text="Age")
    age_label_editor.grid(row=2, column=0, padx=20)

    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0, padx=20)

    email_label_editor = Label(editor, text="Email")
    email_label_editor.grid(row=4, column=0, padx=20)

    pass_label_editor = Label(editor, text="Password")
    pass_label_editor.grid(row=5, column=0, padx=20)

    # Loop through results
    for record in records:
        f_name_editor.insert(0, record[1])
        f_lname_editor.insert(0, record[2])
        age_editor.insert(0, record[3])
        city_editor.insert(0, record[4])
        email_editor.insert(0, record[5])
        password_editor.insert(0, record[6])

    # Create a Save Button To Save edited record
    save = Button(editor, text="Save Records", command=u_update)
    save.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

    # clear the txt boxes
    ud_user_id.delete(0, END)

    conn.commit()

    conn.close()


def users_update():
    global ud_user_id
    global ud_user_id_label
    global ud_submit_btn

    delete_label = Label(wli.up_frame, text="Please see which ID corresponds to the user you want to update and insert "
                                            "it")
    delete_label.grid(row=0, column=3)

    # create text boxes
    ud_user_id = Entry(wli.up_frame, width=30)
    ud_user_id.grid(row=1, column=4, padx=20, pady=10)

    # create text boxes labels
    ud_user_id_label = Label(wli.up_frame, text="User id: ")
    ud_user_id_label.grid(row=1, column=3)

    # create submit button
    try:
        ud_submit_btn = Button(wli.up_frame, text="Update record", command=users_update_submit)
        ud_submit_btn.grid(row=6, column=3, columnspan=2, pady=10, padx=10)
    except sqlite3.IntegrityError as e:
        tkinter.messagebox.showerror("Invalid options", "You did not insert a valid option!")


def videos_update_submit():
    pass


def videos_update():
    pass


def login_update_submit():
    pass


def login_update():
    pass


def video_comment_update_submit():
    pass


def video_comment_update():
    pass

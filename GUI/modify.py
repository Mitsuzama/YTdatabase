import tkinter
from tkinter import *
import sqlite3
import GUI.window_log_in as wli


# DONE
def users_submit():
    conn = sqlite3.connect('yt_database.db')

    c = conn.cursor()

    # insert into table
    c.execute("INSERT INTO users(first_name, last_name, age, city, email, role_type) VALUES (:first_name, :last_name, "
              ":age,:city, :email, :role_type)",
              {
                  'first_name': ui_f_name.get(),
                  'last_name': ui_f_lname.get(),
                  'age': ui_age.get(),
                  'city': ui_city.get(),
                  'email': ui_email.get(),
                  'role_type': 'user'
              })
    c.execute("INSERT INTO login_account(username, user_password) VALUES (:username, :user_password)",
              {
                  'username': ui_f_name.get(),
                  'user_password': ui_password.get()
              })

    # clear the txt boxes
    ui_f_name.delete(0, END)
    ui_f_lname.delete(0, END)
    ui_age.delete(0, END)
    ui_city.delete(0, END)
    ui_email.delete(0, END)
    ui_password.delete(0, END)

    conn.commit()

    conn.close()


# DONE
def users_insert():
    global ui_f_name, ui_f_lname, ui_age, ui_city, ui_email, ui_password, ui_pass_label
    global ui_f_name_label, ui_f_lname_label, ui_age_label, ui_city_label, ui_email_label

    # create text boxes
    ui_f_name = Entry(wli.up_frame, width=30)
    ui_f_name.grid(row=0, column=4, padx=20, pady=10)

    ui_f_lname = Entry(wli.up_frame, width=30)
    ui_f_lname.grid(row=1, column=4, padx=20, pady=10)

    ui_age = Entry(wli.up_frame, width=30)
    ui_age.grid(row=2, column=4, padx=20, pady=10)

    ui_city = Entry(wli.up_frame, width=30)
    ui_city.grid(row=3, column=4, padx=20, pady=10)

    ui_email = Entry(wli.up_frame, width=30)
    ui_email.grid(row=4, column=4, padx=20, pady=10)

    ui_password = Entry(wli.up_frame, width=30)
    ui_password.grid(row=5, column=4, padx=20, pady=10)

    # create text boxes labels
    ui_f_name_label = Label(wli.up_frame, text="First name")
    ui_f_name_label.grid(row=0, column=3)

    ui_f_lname_label = Label(wli.up_frame, text="Last name")
    ui_f_lname_label.grid(row=1, column=3)

    ui_age_label = Label(wli.up_frame, text="Age")
    ui_age_label.grid(row=2, column=3)

    ui_city_label = Label(wli.up_frame, text="City")
    ui_city_label.grid(row=3, column=3)

    ui_email_label = Label(wli.up_frame, text="Email")
    ui_email_label.grid(row=4, column=3)

    ui_pass_label = Label(wli.up_frame, text="Password")
    ui_pass_label.grid(row=5, column=3)

    # create submit button
    try:
        ui_submit_btn = Button(wli.up_frame, text="Add record", command=users_submit)
        ui_submit_btn.grid(row=6, column=3, columnspan=2, pady=10, padx=10)
    except sqlite3.IntegrityError as e:
        tkinter.messagebox.showerror("Invalid options", "You did not insert a valid option!")


# DONE
def videos_submit():
    conn = sqlite3.connect('yt_database.db')

    c = conn.cursor()

    # insert into table
    c.execute("INSERT INTO videos(title, user_id, no_of_likes) "
              "VALUES (:title, :user_id, :no_of_likes)",
              {
                  'title': vi_title.get(),
                  'user_id': vi_user_id.get(),
                  'no_of_likes': vi_no_of_likes.get()
              })

    # clear the txt boxes
    vi_title.delete(0, END)
    vi_user_id.delete(0, END)
    vi_no_of_likes.delete(0, END)

    conn.commit()

    conn.close()


# DONE
def videos_insert():
    global vi_title, vi_user_id, vi_no_of_likes
    global vi_title_label, vi_user_id_label, vi_no_of_likes_label

    # create text boxes
    vi_title = Entry(wli.up_frame, width=30)
    vi_title.grid(row=0, column=4, padx=20, pady=10)

    vi_user_id = Entry(wli.up_frame, width=30)
    vi_user_id.grid(row=1, column=4, padx=20, pady=10)

    vi_no_of_likes = Entry(wli.up_frame, width=30)
    vi_no_of_likes.grid(row=2, column=4, padx=20, pady=10)

    # create text boxes labels
    vi_title_label = Label(wli.up_frame, text="Title: ")
    vi_title_label.grid(row=0, column=3)

    vi_user_id_label = Label(wli.up_frame, text="User id:")
    vi_user_id_label.grid(row=1, column=3)

    vi_no_of_likes_label = Label(wli.up_frame, text="Number of likes: ")
    vi_no_of_likes_label.grid(row=2, column=3)

    # create submit button
    try:
        vi_submit_btn = Button(wli.up_frame, text="Add record", command=videos_submit)
        vi_submit_btn.grid(row=6, column=3, columnspan=2, pady=10, padx=10)
    except sqlite3.IntegrityError as e:
        tkinter.messagebox.showerror("Invalid options", "You did not insert a valid option!")


# DONE
def login_submit():
    conn = sqlite3.connect('yt_database.db')

    c = conn.cursor()

    # insert into table
    c.execute("INSERT INTO login_account(username, user_password) "
              "VALUES (:username, :user_password)",
              {
                  'username': ls_username.get(),
                  'user_password': ls_user_password.get()
              })

    # clear the txt boxes
    ls_username.delete(0, END)
    ls_user_password.delete(0, END)

    conn.commit()

    conn.close()


# DONE
def login_insert():
    global ls_username, ls_user_password
    global ls_username_label, ls_user_password_label

    # create text boxes
    ls_username = Entry(wli.up_frame, width=30)
    ls_username.grid(row=0, column=4, padx=20, pady=10)

    ls_user_password = Entry(wli.up_frame, width=30)
    ls_user_password.grid(row=1, column=4, padx=20, pady=10)

    # create text boxes labels
    ls_username_label = Label(wli.up_frame, text="Username: ")
    ls_username_label.grid(row=0, column=3)

    ls_user_password_label = Label(wli.up_frame, text="Password:")
    ls_user_password_label.grid(row=1, column=3)

    # create submit button
    try:
        ls_submit_btn = Button(wli.up_frame, text="Add record", command=login_submit)
        ls_submit_btn.grid(row=6, column=3, columnspan=2, pady=10, padx=10)
    except sqlite3.IntegrityError as e:
        tkinter.messagebox.showerror("Invalid options", "You did not insert a valid option!")


# DONE
def video_comment_submit():
    conn = sqlite3.connect('yt_database.db')

    c = conn.cursor()

    # insert into table
    c.execute("INSERT INTO video_comment(user_id, video_id, comments) "
              "VALUES (:user_id, :video_id, :comments)",
              {
                  'user_id': vc_user_id.get(),
                  'video_id': vc_video_id.get(),
                  'comments': vc_comments.get()
              })

    # clear the txt boxes
    vc_user_id.delete(0, END)
    vc_video_id.delete(0, END)
    vc_comments.delete(0, END)

    conn.commit()

    conn.close()


# DONE
def video_comment_insert():
    global vc_user_id, vc_video_id, vc_comments
    global vc_user_id_label, vc_video_id_label, vc_comments_label

    # create text boxes
    vc_user_id = Entry(wli.up_frame, width=30)
    vc_user_id.grid(row=0, column=4, padx=20, pady=10)

    vc_video_id = Entry(wli.up_frame, width=30)
    vc_video_id.grid(row=1, column=4, padx=20, pady=10)

    vc_comments = Entry(wli.up_frame, width=30)
    vc_comments.grid(row=2, column=4, padx=20, pady=10)

    # create text boxes labels
    vc_user_id_label = Label(wli.up_frame, text="User who wrote the comment: ")
    vc_user_id_label.grid(row=0, column=3)

    vc_video_id_label = Label(wli.up_frame, text="Video id:")
    vc_video_id_label.grid(row=1, column=3)

    vc_comments_label = Label(wli.up_frame, text="Comment: ")
    vc_comments_label.grid(row=2, column=3)

    # create submit button
    try:
        vi_submit_btn = Button(wli.up_frame, text="Add record", command=video_comment_submit)
        vi_submit_btn.grid(row=6, column=3, columnspan=2, pady=10, padx=10)
    except sqlite3.IntegrityError as e:
        tkinter.messagebox.showerror("Invalid options", "You did not insert a valid option!")

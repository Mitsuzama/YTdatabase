import tkinter
from tkinter import *
import sqlite3
import GUI.window_log_in as wli


# DONE
def users_delete_submit():
    conn = sqlite3.connect('yt_database.db')

    c = conn.cursor()

    # insert into table
    c.execute("DELETE FROM users WHERE oid=(:user_id)",
              {
                  'user_id': ud_user_id.get()
              })

    # clear the txt boxes
    ud_user_id.delete(0, END)

    conn.commit()

    conn.close()


# DONE
def users_delete():
    global ud_user_id
    global ud_user_id_label

    delete_label = Label(wli.up_frame, text="Please see which ID coresponds to the user you want to delete and insert "
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
        ud_submit_btn = Button(wli.up_frame, text="Delete record", command=users_delete_submit)
        ud_submit_btn.grid(row=6, column=3, columnspan=2, pady=10, padx=10)
    except sqlite3.IntegrityError as e:
        tkinter.messagebox.showerror("Invalid options", "You did not insert a valid option!")


# DONE
def videos_delete_submit():
    conn = sqlite3.connect('yt_database.db')

    c = conn.cursor()

    # insert into table
    c.execute("DELETE FROM videos WHERE oid=(:video_id)",
              {
                  'video_id': vd_video_id.get()
              })

    # clear the txt boxes
    vd_video_id.delete(0, END)

    conn.commit()

    conn.close()


# DONE
def videos_delete():
    global vd_video_id
    global vd_video_id_label

    delete_label = Label(wli.up_frame, text="Please see which ID coresponds to the video you want to delete and insert "
                                            "it")
    delete_label.grid(row=0, column=3)

    # create text boxes
    vd_video_id = Entry(wli.up_frame, width=30)
    vd_video_id.grid(row=1, column=4, padx=20, pady=10)

    # create text boxes labels
    vd_video_id_label = Label(wli.up_frame, text="User id: ")
    vd_video_id_label.grid(row=1, column=3)

    # create submit button
    try:
        vd_submit_btn = Button(wli.up_frame, text="Delete record", command=videos_delete_submit)
        vd_submit_btn.grid(row=6, column=3, columnspan=2, pady=10, padx=10)
    except sqlite3.IntegrityError as e:
        tkinter.messagebox.showerror("Invalid options", "You did not insert a valid option!")


def login_delete_submit():
    conn = sqlite3.connect('yt_database.db')

    c = conn.cursor()

    # insert into table
    c.execute("DELETE FROM login_account WHERE oid=(:user_id)",
              {
                  'user_id': ld_user_id.get()
              })
    c.execute("DELETE FROM users WHERE oid=(:user_id)",
              {
                  'user_id': ld_user_id.get()
              })

    # clear the txt boxes
    ld_user_id.delete(0, END)

    conn.commit()

    conn.close()


def login_delete():
    global ld_user_id
    global ld_user_id_label

    delete_label = Label(wli.up_frame, text="Please see which ID coresponds to the user you want to delete and insert "
                                            "it")
    delete_label.grid(row=0, column=3)

    # create text boxes
    ld_user_id = Entry(wli.up_frame, width=30)
    ld_user_id.grid(row=1, column=4, padx=20, pady=10)

    # create text boxes labels
    ld_user_id_label = Label(wli.up_frame, text="User id: ")
    ld_user_id_label.grid(row=1, column=3)

    # create submit button
    try:
        ud_submit_btn = Button(wli.up_frame, text="Delete record", command=login_delete_submit)
        ud_submit_btn.grid(row=6, column=3, columnspan=2, pady=10, padx=10)
    except sqlite3.IntegrityError as e:
        tkinter.messagebox.showerror("Invalid options", "You did not insert a valid option!")


# DONE
def video_comment_delete_submit():
    conn = sqlite3.connect('yt_database.db')

    c = conn.cursor()

    # insert into table
    c.execute("DELETE FROM video_comment WHERE oid=(:comment_id)",
              {
                  'comment_id': vcd_comment_id.get()
              })

    # clear the txt boxes
    vcd_comment_id.delete(0, END)

    conn.commit()

    conn.close()


# DONE
def video_comment_delete():
    global vcd_comment_id
    global vcd_comment_id_label

    delete_label = Label(wli.up_frame, text="Please see which ID coresponds to the comment you want to delete and "
                                            "insert it")
    delete_label.grid(row=0, column=3)

    # create text boxes
    vcd_comment_id = Entry(wli.up_frame, width=30)
    vcd_comment_id.grid(row=1, column=4, padx=20, pady=10)

    # create text boxes labels
    vcd_comment_id_label = Label(wli.up_frame, text="Comment id: ")
    vcd_comment_id_label.grid(row=1, column=3)

    # create submit button
    try:
        ud_submit_btn = Button(wli.up_frame, text="Delete record", command=video_comment_delete_submit)
        ud_submit_btn.grid(row=6, column=3, columnspan=2, pady=10, padx=10)
    except sqlite3.IntegrityError as e:
        tkinter.messagebox.showerror("Invalid options", "You did not insert a valid option!")

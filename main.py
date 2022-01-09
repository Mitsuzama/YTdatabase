import tkinter
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

import GUI.window_log_in as wli
import GUI.window_sign_up as wsu

import Utility.Crypt as cr
import Utility.table_management as tm


class PyApp(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(0, 0)
        self.geometry("400x300")
        self.title('YouTube database')
        self.iconbitmap('Images/ytDatabaseIcon.ico')
        self.eval('tk::PlaceWindow . center')

        self.width = 400
        self.height = 300

        scr_width = self.winfo_screenwidth()
        scr_height = self.winfo_screenheight()

        x = (scr_width / 2) - (self.width / 2)
        y = (scr_height / 2) - (self.height / 2)

        self.geometry(f'{self.width}x{self.height}+{int(x)}+{int(y)}')

        self.initGUI()

    def initGUI(self):
        # connect to db
        conn = sqlite3.connect('yt_database.db')

        # create cursor instance
        c = conn.cursor()

        tm.dropTables()

        # create the tables
        tm.createTables()

        # insert into tables
        tm.insertIntoTables()

        welcome_image = ImageTk.PhotoImage(Image.open("Images/welcome.PNG"))
        welcome_image_label = Label(self, image=welcome_image, height=70, width=200)
        welcome_image_label.grid(row=0, column=0)

        # username
        username_label = Label(self, text="Username:")
        username_label.grid(row=1, column=0, padx=20)

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, padx=20, pady=10)

        # password
        password_label = Label(self, text="Password:")
        password_label.grid(row=2, column=0, padx=20)

        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, padx=20, pady=10)

        # login
        self.login_button = Button(self, text="Login", command=self.open_login)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

        # sign up
        sign_up_button = Button(self, text="Sign Up", command=wsu.openWinLogin)
        sign_up_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

        # quit
        quit_button = Button(self, text="Quit", command=self.quit)
        quit_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

        # login try

        # commit changes
        conn.commit()

        conn.close()

    def open_login(self):
        # connect to db
        conn = sqlite3.connect('yt_database.db')

        # create cursor instance
        c = conn.cursor()

        username_txt = self.username_entry.get()
        password_txt = self.password_entry.get()

        encode = cr.encrypt(password_txt)

        wli.openWinDb()

        conn.commit()
        conn.close()


def main():
    window_login = PyApp()
    window_login.mainloop()


if __name__ == '__main__':
    main()

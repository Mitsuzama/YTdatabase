import tkinter
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import window_log_in
import window_sign_up
from table_management import *

def open_login():
    # connect to db
    conn = sqlite3.connect('yt_database.db')

    # create cursor instance
    c = conn.cursor()

    window_sign_up.openWinLogin()

    conn.commit()
    conn.close()

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

        dropTables()

        # create the tables
        createTables()

        # insert into tables
        insertIntoTables()

        welcome_image = ImageTk.PhotoImage(Image.open("Images/welcome.PNG"))
        welcome_image_label = Label(self, image=welcome_image, height=70, width=200)
        welcome_image_label.grid(row=0, column=0)

        # username
        username_label = Label(self, text="Username:")
        username_label.grid(row=1, column=0, padx=20)

        username_entry = Entry(self)
        username_entry.grid(row=1, column=1, padx=20, pady=10)

        # password
        password_label = Label(self, text="Password:")
        password_label.grid(row=2, column=0, padx=20)

        password_entry = Entry(self, show="*")
        password_entry.grid(row=2, column=1, padx=20, pady=10)

        # login
        login_button = Button(self, text="Login", command=window_log_in.openWinDb)
        login_button.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

        # sign up
        sign_up_button = Button(self, text="Sign Up", command=open_login)
        sign_up_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

        # quit
        quit_button = Button(self, text="Quit", command=self.quit)
        quit_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

        # commit changes
        conn.commit()

        conn.close()


def main():
    window_login = PyApp()
    window_login.mainloop()


if __name__ == '__main__':
    main()

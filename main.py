import tkinter
from tkinter import *
from PIL import ImageTk, Image


class PyApp(tkinter.Tk):

    def __init__(self):
        super().__init__()

        self.resizable(0, 0)
        self.geometry("900x600")
        self.title('YouTube database')
        self.iconbitmap('Images/ytDatabaseIcon.ico')

        self.columnconfigure(0, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)

        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, pad=5)
        self.rowconfigure(4, pad=5)
        self.rowconfigure(5, pad=5)


        self.initGUI()

    def initGUI(self):
        frame = Frame(self, borderwidth=10)

        welcome_image = ImageTk.PhotoImage(Image.open('Images/welcome.PNG'))
        welcome_image_label = Label(image=welcome_image, height=166, width=410)
        welcome_image_label.grid(row=0, column=1)

        # username
        username_label = Label(self, text="Username:")
        username_label.grid(row=2, column=1, padx=5, pady=5)

        username_entry = Entry(self, text="please insert your username")
        username_entry.grid(row=2, column=2, padx=5, pady=5)

        # password
        password_label = Label(self, text="Password:")
        password_label.grid(row=3, column=1, padx=5, pady=5)

        password_entry = Entry(self, show="*")
        password_entry.grid(row=3, column=2, padx=5, pady=5)

        # login
        login_button = Button(self, text="Login")
        login_button.grid(row=4, column=2, sticky=tkinter.S, padx=5, pady=5)

        # quit
        quit_button = Button(self, text="Quit", command=self.quit)
        quit_button.grid(row=6, column=2, sticky=tkinter.S, padx=5, pady=5)

    def __login_command(self):
        pass


def main():
    #root = Tk()
    main_frame = PyApp()

    main_frame.mainloop()


if __name__ == '__main__':
    main()

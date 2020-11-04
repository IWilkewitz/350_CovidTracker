import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.info = tk.Button(self)
        self.info["text"] = "LOGIN"
        self.info["command"] = self.say_hi
        self.info.pack(side="top")

        self.info = tk.Button(self)
        self.info["text"] = "User info button"
        self.info["command"] = self.info
        self.info.pack(side="left")

        self.info = tk.Button(self)
        self.info["text"] = "News button"
        self.info["command"] = self.news
        self.info.pack(side="right")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


    def say_hi(self):
        master = tk.Tk()
        tk.Label(master, text="First Name").grid(row=0)
        tk.Label(master, text="Last Name").grid(row=1)

        e1 = tk.Entry(master)
        e2 = tk.Entry(master)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        master.mainloop()

    def info(self):
        print("This leads to user info")

    def news(self):
        print("This leads to news")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
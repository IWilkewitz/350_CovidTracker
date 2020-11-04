import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top", pady=25, padx=25)

        self.info = tk.Button(self)
        self.info["text"] = "User info button"
        self.info["command"] = self.infoscreen
        self.info.pack(side="left", pady=25, padx=25)

        self.info = tk.Button(self)
        self.info["text"] = "News button"
        self.info["command"] = self.news
        self.info.pack(side="right", pady=25, padx=25)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom", pady=25, padx=25)

    def say_hi(self):
        print("hi there, everyone!")

    def infoscreen(self):
        print("This leads to user info")

    def news(self):
        print("This leads to news")


root = tk.Tk()
app = Application(master=root)
root.geometry('700x300')
app.mainloop()
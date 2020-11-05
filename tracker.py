import tkinter as tk
import tkinter.ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.login = tk.Button(self)
        self.login["text"] = "Login"
        self.login["command"] = self.loginpage
        self.login.grid(row=1, column=1, pady=5)

        self.info = tk.Button(self)
        self.info["text"] = "User info button"
        self.info["command"] = self.infopage
        self.info.grid(row=2, column=0, pady=5, padx=5)

        self.info = tk.Button(self)
        self.info["text"] = "News button"
        self.info["command"] = self.news
        self.info.grid(row=2, column=2, padx=5)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=3, column=1, pady=5)

    def loginpage(self):
        loginWindow = tk.Toplevel(root)
        loginWindow.title("Login Window")
        loginWindow.geometry("250x100")

        tk.Label(loginWindow, text="Username: ").grid(row=0, pady=5)
        tk.Label(loginWindow, text="Password: ").grid(row=1)

        tk.Entry(loginWindow).grid(row=0, column=1)
        tk.Entry(loginWindow).grid(row=1, column=1)

        #This button closes the login screen
        loginQuit = tk.Button(loginWindow)
        loginQuit["text"] = "Back"
        loginQuit["command"] = loginWindow.destroy
        loginQuit.grid(row=2, column=0, pady=15)

        #Forgot password button
        forPas = tk.Button(loginWindow)
        forPas["text"] = "Forgot Password"
        forPas["command"] = self.resPas
        forPas.grid(row=2, column=1)

        #Login button
        logBut = tk.Button(loginWindow)
        logBut["text"] = "Login"
        logBut["command"] = self.userLogin
        logBut.grid(row=2, column=3)

        #not sure if this line is needed but i'll keep it around just in case
        #tk.mainloop()


    #placeholder button functions
    def infopage(self):
        print("This leads to user info")

    def news(self):
        print("This leads to news")

    def resPas(self):
        print("Reset Password Path")

    def userLogin(self):
        print("This leads to the user's homepage (when legitimate credentials are inputted)")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
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

        # #Login button
        logBut = tk.Button(loginWindow)
        logBut["text"] = "Sign In"
        logBut["command"] = self.appPage
        logBut.grid(row=2, column=3)

        #not sure if this line is needed but i'll keep it around just in case
        #tk.mainloop()

    def appPage(self):
        appPage = tk.Toplevel(root)
        appPage.title("Application")
        appPage.geometry("250x100")

        appQuit = tk.Button(appPage)
        appQuit["text"] = "Back"
        appQuit["command"] = appPage.destroy
        appQuit.grid(row=2, column=0, pady=15)

        survey = tk.Button(appPage)
        survey["text"] = "Survey"
        survey["command"] = appPage.destroy
        survey.grid(row=2, column=2)

        UserInfo = tk.Button(appPage)
        UserInfo["text"] = "User Info"
        UserInfo["command"] = appPage.destroy
        UserInfo.grid(row=2, column=3)

        news = tk.Button(appPage)
        news["text"] = "News"
        news["command"] = appPage.destroy
        news.grid(row=2, column=4)
        # tk.Label(loginWindow, text="Username: ").grid(row=0, pady=5)
        # tk.Label(loginWindow, text="Password: ").grid(row=1)

        # tk.Entry(loginWindow).grid(row=0, column=1)
        # tk.Entry(loginWindow).grid(row=1, column=1)

        # #This button closes the login screen
        # loginQuit = tk.Button(loginWindow)
        # loginQuit["text"] = "NEWS"
        # loginQuit["command"] = loginWindow.destroy
        # loginQuit.grid(row=2, column=0, pady=15)

        # #Forgot password button
        # forPas = tk.Button(loginWindow)
        # forPas["text"] = "SURVEY"
        # forPas["command"] = self.resPas
        # forPas.grid(row=2, column=1)

        # #Login button
        # logBut = tk.Button(loginWindow)
        # logBut["text"] = "Sign In"
        # logBut["command"] = self.userLogin
        # logBut.grid(row=2, column=3)

        #placeholder button functions
    def infopage(self):
        print("This leads to user info")

    def news(self):
        print("This leads to news")

    def resPas(self):
        print("This leads to theReset Password Path")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
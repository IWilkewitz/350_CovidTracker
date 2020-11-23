import tkinter as tk
import tkinter.ttk
from tkinter import Tk, Canvas, Frame, BOTH
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #create_widgets.geometry("450x400")

        self.title = tk.Label(self, text="Welcome to MegaTrace", font=("Helvetica", 24))
        self.title.grid(row=0, column=1, pady=25)
        self.title = tk.Label(self, text="Please sign in to continue:", font=("Helvetica", 16))
        self.title.grid(row=1, column=1, pady=0)

        self.login = tk.Button(self)
        self.login["text"] = "Login"
        self.login["font"] = ("Helvetica", 12, "bold")
        self.login["command"] = self.loginpage
        self.login.grid(row=2, column=1, pady=5)
        self.login.config(width=35, height=3)

        self.signUp = tk.Button(self)
        self.signUp["text"] = "Sign Up"
        self.signUp["font"] = ("Helvetica", 12, "bold")
        self.signUp["command"] = self.signUpPage
        self.signUp.grid(row=3, column=1, pady=5)
        self.signUp.config(width=35, height=3)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=4, column=1, pady=5)
        self.quit.config(width=35, height=3)
        self.quit["font"] = ("Helvetica", 12, "bold")



    def signUpPage2(self):
        signUpWindow2 = tk.Toplevel(root)
        signUpWindow2.title("Sign Up")
        signUpWindow2.geometry("450x400")

        tk.Label(signUpWindow2, text="First Name: ", font=("Helvetica", 16)).grid(row=0,column=1, pady=5)
        tk.Label(signUpWindow2, text="Last Name: ", font=("Helvetica", 16)).grid(row=2, column=1, pady=5)
        tk.Label(signUpWindow2, text="Date of Birth (MM/DD/YYYY): ", font=("Helvetica", 16)).grid(row=4,column=1, pady=5)
        tk.Label(signUpWindow2, text="Email: ", font=("Helvetica", 16)).grid(row=6,column=1, pady=5)
        tk.Label(signUpWindow2, text="Phone Number: ", font=("Helvetica", 16)).grid(row=8, column=1, pady=5)

        tk.Entry(signUpWindow2, width=50).grid(row=1, column=1, pady=5)
        tk.Entry(signUpWindow2, show="•", width=50).grid(row=3, column=1, pady=5)
        tk.Entry(signUpWindow2, show="•", width=50).grid(row=5, column=1, pady=5)
        tk.Entry(signUpWindow2, show="•", width=50).grid(row=7, column=1, pady=5)
        tk.Entry(signUpWindow2, show="•", width=50).grid(row=9, column=1, pady=5)

        # #NextPage button
        nextStep2 = tk.Button(signUpWindow2, width=30, height=3)
        nextStep2["text"] = "Sign Up!"
        nextStep2["command"] = self.appPage
        nextStep2["font"] = ("Helvetica", 12, "bold")
        nextStep2.grid(row=10, column=1, pady=5)
        nextStep2.config(width=35, height=3)

    def signUpPage(self):
        signUpWindow = tk.Toplevel(root)
        signUpWindow.title("Sign Up")
        signUpWindow.geometry("450x400")
        usernameInfo = tk.Label(signUpWindow, text="(Must Be Minimum of 8 characters)", font=("Helvetica", 12))
        usernameInfo.grid(row=4, column=1, pady=5)
        tk.Label(signUpWindow, text="Choose a Username: ", font=("Helvetica", 16)).grid(row=0,column=1, pady=5)
        tk.Label(signUpWindow, text="Choose a Password: ", font=("Helvetica", 16)).grid(row=2, column=1, pady=5)

        tk.Entry(signUpWindow, width=50).grid(row=1, column=1, pady=5)
        tk.Entry(signUpWindow, show="•", width=50).grid(row=3, column=1, pady=5)

        # #NextPage button
        nextStep = tk.Button(signUpWindow, width=30, height=3)
        nextStep["text"] = "Next"
        nextStep["command"] = self.signUpPage2
        nextStep["font"] = ("Helvetica", 12, "bold")
        nextStep.grid(row=5, column=1, pady=5)
        nextStep.config(width=35, height=3)

    def loginpage(self):
        loginWindow = tk.Toplevel(root)
        loginWindow.title("Login Window")
        loginWindow.geometry("450x400")

        tk.Label(loginWindow, text="Username: ", font=("Helvetica", 16)).grid(row=0, pady=5)
        tk.Label(loginWindow, text="Password: ", font=("Helvetica", 16)).grid(row=1)

        tk.Entry(loginWindow, width=50).grid(row=0, column=1)
        tk.Entry(loginWindow, show="•", width=50).grid(row=1, column=1)

        #This button closes the login screen
        loginQuit = tk.Button(loginWindow, width=30, height=3)
        loginQuit["text"] = "Back"
        loginQuit["command"] = loginWindow.destroy
        loginQuit["font"] = ("Helvetica", 12, "bold")
        loginQuit.grid(row=4, column=1, pady=15)

        #Forgot password button
        forPas = tk.Button(loginWindow, width=30, height=3)
        forPas["text"] = "Forgot Password"
        forPas["command"] = self.forgotPass
        forPas["font"] = ("Helvetica", 12, "bold")
        forPas.grid(row=3, column=1, pady=15)

        # #Login button
        logBut = tk.Button(loginWindow, width=30, height=3)
        logBut["text"] = "Login"
        logBut["command"] = self.appPage
        logBut["font"] = ("Helvetica", 12, "bold")
        logBut.grid(row=2, column=1, pady=15)

    def appPage(self):
        appPage = tk.Toplevel(root)
        appPage.title("Application")
        appPage.geometry("450x400")

        label = tk.Label(appPage, text="Home Screen", font=("Helvetica", 24))
        label.grid(row=0, column=1)

        appQuit = tk.Button(appPage, width=42, height=3)
        appQuit["text"] = "Log Out"
        appQuit["command"] = appPage.destroy
        appQuit["font"] = ("Helvetica", 12, "bold")
        appQuit.grid(row=4, column=1, pady=10)

        survey = tk.Button(appPage, width=42, height=3)
        survey["text"] = "Survey"
        survey["command"] = self.survey
        survey["font"] = ("Helvetica", 12, "bold")
        survey.grid(row=3, column=1, padx=10, pady=10)

        UserInfo = tk.Button(appPage, width=42, height=3)
        UserInfo["text"] = "User Info"
        UserInfo["command"] = self.userPage
        UserInfo["font"] = ("Helvetica", 12, "bold")
        UserInfo.grid(row=2, column=1, padx=10, pady=10)

        news = tk.Button(appPage, width=42, height=3)
        news["text"] = "News"
        news["command"] = self.newsPage
        news["font"] = ("Helvetica", 12, "bold")
        news.grid(row=1, column=1, padx=10, pady=10)

    def forgotPass(self):
        forPass = tk.Toplevel(root)
        forPass.title("Forgot Password")
        forPass.geometry("450x400")

        tk.Label(forPass, text="Enter Your Email: ", font=("Helvetica", 16)).grid(row=0,column=1, pady=5)
        tk.Label(forPass, text="Enter Your Phone Number: ", font=("Helvetica", 16)).grid(row=2, column=1, pady=5)

        tk.Entry(forPass, width=50).grid(row=1, column=1, pady=5)
        tk.Entry(forPass, show="•", width=50).grid(row=3, column=1, pady=5)

    def userPage(self):
        usrInfo = tk.Toplevel(root)
        usrInfo.geometry("450x400")

        #canvas = Canvas(usrInfo)
        #canvas.create_rectangle(170, 20, 280, 120)

        tk.Label(usrInfo, text="First Name: ", font=("Helvetica", 16)).grid(row=5,column=0, pady=5)
        tk.Label(usrInfo, text="Last Name: ", font=("Helvetica", 16)).grid(row=6, column=0, pady=5)
        tk.Label(usrInfo, text="Date of Birth (MM/DD/YYYY): ", font=("Helvetica", 16)).grid(row=7,column=0, pady=5)
        tk.Label(usrInfo, text="Email: ", font=("Helvetica", 16)).grid(row=8,column=0, pady=5)
        tk.Label(usrInfo, text="Phone Number: ", font=("Helvetica", 16)).grid(row=9, column=0, pady=5)
        tk.Label(usrInfo, text="Address: ", font=("Helvetica", 16)).grid(row=10,column=0, pady=5)
        
        # #NextPage button
        edit = tk.Button(usrInfo, width=30, height=3)
        edit["text"] = "Edit User Profile"
        edit["command"] = self.signUpPage2
        edit["font"] = ("Helvetica", 12, "bold")
        edit.grid(row=11, column=0, pady=5)
        edit.config(width=35, height=3)


    def newsPage(self):
        newsPage = tk.Toplevel(root)
        newsPage.title("COVID-19 NEWS")
        newsPage.geometry("450x400")

    def survey(self):
        surPage = tk.Toplevel(root)
        surPage.title("COVID-19 Survey")
        surPage.geometry("450x400")

        yes = tk.Button(surPage)
        yes["text"] = "YES"
        yes["command"] = surPage.destroy
        yes.grid(row=1, column=1, pady=5)

        no = tk.Button(surPage)
        no["text"] = "NO"
        no["command"] = surPage.destroy
        no.grid(row=3, column=1, pady=5)

root = tk.Tk()
root.geometry("450x400")
#root.configure(bg='#8cdbed')
root.title("MegaTrace")
app = Application(master=root)
app.mainloop()

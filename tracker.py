import tkinter as tk
import tkinter.ttk
from tkinter import Tk, Canvas, Frame, BOTH
import time as tm
import datetime as dt
import re
from getpass import getpass
#import urllib.request
#import bs4

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
        tk.Entry(signUpWindow2, width=50).grid(row=3, column=1, pady=5)
        tk.Entry(signUpWindow2, width=50).grid(row=5, column=1, pady=5)
        tk.Entry(signUpWindow2, width=50).grid(row=7, column=1, pady=5)
        tk.Entry(signUpWindow2, width=50).grid(row=9, column=1, pady=5)

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
        usernameInfo = tk.Label(signUpWindow, text="(8 characters: 1+ uppercase, 1+ number)", font=("Helvetica", 12))
        usernameInfo.grid(row=4, column=1, pady=5)
        tk.Label(signUpWindow, text="Choose a Username: ", font=("Helvetica", 16)).grid(row=0,column=1, pady=5)
        tk.Label(signUpWindow, text="Choose a Password: ", font=("Helvetica", 16)).grid(row=2, column=1, pady=5)
        username = tk.Entry(signUpWindow, width=50).grid(row=1, column=1, pady=5)
        password = tk.Entry(signUpWindow, show="•", width=50).grid(row=3, column=1, pady=5)
        print(username)
        if (is_valid_pass(password)):
            print(password)

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
        tk.Entry(loginWindow, show="$", width=50).grid(row=1, column=1)

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

        tk.Label(forPass, text="Enter Email: ", font=("Helvetica", 12)).grid(row=0,column=0, pady=5)
        tk.Label(forPass, text="Enter Phone Number:", font=("Helvetica", 12)).grid(row=1, column=0, pady=5)

        tk.Entry(forPass, width=40).grid(row=0, column=1, pady=5)
        tk.Entry(forPass, show="•", width=40).grid(row=1, column=1, pady=5)

        forLink = tk.Button(forPass, width=15, height=3)
        forLink["text"] = "Send Reset Link"
        forLink["command"] = self.destroy
        forLink["font"] = ("Helvetica", 10, "bold")
        forLink.grid(row=2, column=1, padx=10, pady=10)

    def editUsr(self):
        editPge = tk.Toplevel(root)
        editPge.title("Sign Up")
        editPge.geometry("450x450")

        tk.Label(editPge, text="First Name: ", font=("Helvetica", 16)).grid(row=0,column=1, pady=5)
        tk.Label(editPge, text="Last Name: ", font=("Helvetica", 16)).grid(row=2, column=1, pady=5)
        tk.Label(editPge, text="Date of Birth (MM/DD/YYYY): ", font=("Helvetica", 16)).grid(row=4,column=1, pady=5)
        tk.Label(editPge, text="Email: ", font=("Helvetica", 16)).grid(row=6,column=1, pady=5)
        tk.Label(editPge, text="Phone Number: ", font=("Helvetica", 16)).grid(row=8, column=1, pady=5)

        tk.Entry(editPge, width=50).grid(row=1, column=1, pady=5)
        tk.Entry(editPge, show="•", width=50).grid(row=3, column=1, pady=5)
        tk.Entry(editPge, show="•", width=50).grid(row=5, column=1, pady=5)
        tk.Entry(editPge, show="•", width=50).grid(row=7, column=1, pady=5)
        tk.Entry(editPge, show="•", width=50).grid(row=9, column=1, pady=5)

        # #NextPage button
        save = tk.Button(editPge, width=30, height=3)
        save["text"] = "Save Changes"
        save["command"] = self.userPage
        save["font"] = ("Helvetica", 12, "bold")
        save.grid(row=10, column=1, pady=5)
        save.config(width=35, height=3)

    def userPage(self):
        usrInfo = tk.Toplevel(root)
        usrInfo.title("User Profile")
        usrInfo.geometry("450x400")

        #canvas = Canvas(usrInfo)
        #canvas.create_rectangle(170, 20, 280, 120)

        tk.Label(usrInfo, text="First Name: ", font=("Helvetica", 16)).grid(row=5,column=0, pady=5)
        tk.Label(usrInfo, text="Last Name: ", font=("Helvetica", 16)).grid(row=6, column=0, pady=5)
        tk.Label(usrInfo, text="Date of Birth (MM/DD/YYYY): ", font=("Helvetica", 16)).grid(row=7,column=0, pady=5)
        tk.Label(usrInfo, text="Email: ", font=("Helvetica", 16)).grid(row=8,column=0, pady=5)
        tk.Label(usrInfo, text="Phone Number: ", font=("Helvetica", 16)).grid(row=9, column=0, pady=5)
        tk.Label(usrInfo, text="Address: ", font=("Helvetica", 16)).grid(row=10,column=0, pady=5)
        tk.Label(usrInfo, text="Exposure Date: ", font=("Helvetica", 16)).grid(row=11,column=0, pady=5)

        # #NextPage button
        edit = tk.Button(usrInfo, width=30, height=3)
        edit["text"] = "Edit User Profile"
        edit["command"] = self.editUsr
        edit["font"] = ("Helvetica", 12, "bold")
        edit.grid(row=11, column=0, pady=5)
        edit.config(width=35, height=3)

        # profile_quit = tk.Button(usrInfo, width=10, height=2)
        # profile_quit["text"] = "Back"
        # profile_quit["command"] = loginWindow.destroy
        # profile_quit["font"] = ("Helvetica", 12, "bold")
        # profile_quit.grid(row=4, column=2, pady=15)

    def newsPage(self):
        newsPage = tk.Toplevel(root)
        newsPage.title("COVID-19 NEWS")
        newsPage.geometry("450x400")

        """ url = 'https://www.mlive.com/#section__news'
        html = urllib.request.urlopen(url).read()
        parsed = bs4.BeautifulSoup(html, "html.parser")
        data = parsed.find_all("h3")
        headline = ""
        for item in data:
            if("COVID-19" in str(item) or "Coronavirus" in str(item) or "COVID" in str(item)):
                headline = str(item.text.strip())
                break

        tk.Label(newsPage, text="Most Recent Michigan Covid Headline: ", font=("Helvetica", 16)).grid(row=0,column=1, pady=5)
        tk.Label(newsPage, text=str(headline), font=("Helvetica", 12), wraplength=400).grid(row=1,column=1, pady=5)

        url = 'https://news.yahoo.com/'
        html = urllib.request.urlopen(url).read()
        parsed = bs4.BeautifulSoup(html, "html.parser")
        data = parsed.find_all("h3")
        headline = ""
        for item in data:
            if("COVID-19" in str(item) or "Coronavirus" in str(item) or "COVID" in str(item)):
                headline = str(item.text.strip()) """

        tk.Label(newsPage, text="Most Recent National Covid Headline: ", font=("Helvetica", 16)).grid(row=2,column=1, pady=5)
        #tk.Label(newsPage, text=str(headline), font=("Helvetica", 12), wraplength=400).grid(row=3,column=1, pady=5)

        appQuit = tk.Button(newsPage, width=42, height=3)
        appQuit["text"] = "Back"
        appQuit["command"] = newsPage.destroy
        appQuit["font"] = ("Helvetica", 12, "bold")
        appQuit.grid(row=4, column=1, padx=2, pady=1)

        local_time = tm.strftime('%I:%M %p')
        clk_lbl = tk.Label(newsPage, font = 'Helvetica', bg = 'white', fg = 'black', text = local_time)
        clk_lbl.grid(row = 6, column = 1)

    def tracePge(self):
        conTrace = tk.Toplevel(root)
        conTrace.title("Contact Tracing Information")
        conTrace.geometry("450x200")
        tk.Label(conTrace, text="Enter First Name: ", font=("Helvetica", 12)).grid(row=0,column=0, pady=5)
        tk.Label(conTrace, text="Enter Email: ", font=("Helvetica", 12)).grid(row=1,column=0, pady=5)
        tk.Label(conTrace, text="Enter Phone Number:", font=("Helvetica", 12)).grid(row=2, column=0, pady=5)

        tk.Entry(conTrace, width=30).grid(row=0, column=1, pady=5)
        tk.Entry(conTrace, width=30).grid(row=1, column=1, pady=5)
        tk.Entry(conTrace, width=30).grid(row=2, column=1, pady=5)

         # #NextPage button
        addContact = tk.Button(conTrace, width=10, height=3)
        addContact["text"] = "Add"
        addContact["command"] = self.editUsr
        addContact["font"] = ("Helvetica", 12, "bold")
        addContact.grid(row=3, column=0)
        addContact.config(width=10, height=3)

         # #NextPage button
        newContact = tk.Button(conTrace, width=10, height=3)
        newContact["text"] = "New Contact"
        newContact["command"] = self.tracePge
        newContact["font"] = ("Helvetica", 12, "bold")
        newContact.grid(row=3, column=1)
        newContact.config(width=10, height=3)

         # #NextPage button
        doneButton = tk.Button(conTrace, width=10, height=3)
        doneButton["text"] = "Done"
        doneButton["command"] = self.destroy
        doneButton["font"] = ("Helvetica", 12, "bold")
        doneButton.grid(row=3, column=2)
        doneButton.config(width=10, height=3)

    def exposure(self):
        exPage = tk.Toplevel(root)
        exPage.title("COVID-19 Survey")
        exPage.geometry("400x150")

        tk.Label(exPage, text="Possible Exposure Date: ",
        font=("Helvetica", 12)).grid(row=0, column=0, pady=5)
        tk.Entry(exPage, width=40).grid(row=1, column=0, pady=5)

        trace = tk.Button(exPage, width=30, height=3)
        trace["text"] = "StartContact Tracing"
        trace["command"] = self.tracePge
        trace["font"] = ("Helvetica", 12, "bold")
        trace.grid(row=11, column=0, pady=5)
        trace.config(width=35, height=3)

    def survey(self):
        surPage = tk.Toplevel(root)
        surPage.title("COVID-19 Survey")
        surPage.geometry("250x120")

        tk.Label(surPage, text="Have You Had Covid-19? ",
        font=("Helvetica", 16)).grid(row=0, column=1, pady=5)

        yes = tk.Button(surPage)
        yes["text"] = "YES"
        yes["command"] = self.exposure
        yes.grid(row=1, column=1, pady=5)

        no = tk.Button(surPage)
        no["text"] = "NO"
        no["command"] = surPage.destroy
        no.grid(row=2, column=1, pady=5)

def is_valid_pass(password):
        while True:
            password = getpass()
            if len(password) < 8:
                print("Password must be 8 characters.")
            elif re.search('[0-9]', password) is None:
                print("Password must have a number")
            elif re.search('[A-Z]', password) is None:
                print("Password must have one uppercase letter")
            else:
                break

root = tk.Tk()
root.geometry("450x400")
#root.configure(bg='#8cdbed')
root.title("MegaTrace")
app = Application(master=root)
app.mainloop()

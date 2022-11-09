'''
This Module Contains Login Page
'''
from tkinter import *
class login:
    def __init__(self,mainFrame):
        #FRAMES
        self.loginFrame=mainFrame
        labelContainer=Frame(self.loginFrame)
        entryContainer=Frame(self.loginFrame)
        labelContainer.grid(row=1,column=1,padx=10)
        entryContainer.grid(row=1,column=2,padx=10)
        # add a back and a new user button

        #LABELS
        userName=Label(labelContainer,text='User Name: ',font=('Verdana 14'))
        password=Label(labelContainer,text='Password: ',font=('Verdana 14'))
        userName.grid(row=1,column=1)
        password.grid(row=2,column=1)

        #ENTRY
        userNameEntry=Entry(entryContainer)
        passwordEntry=Entry(entryContainer,show='*')
        userNameEntry.grid(row=1,column=1)
        passwordEntry.grid(row=2,column=1)


    def openWin(self,mainFrame):
        return login(mainFrame)

    
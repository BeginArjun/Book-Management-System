'''
This Module Contains Registration Window
'''
from tkinter import *
from src import users
from src import database
class registerWin:
    def __init__(self,mainFrame):
        self.registerFrame=mainFrame
        labelFrame=Frame(mainFrame)
        entryFrame=Frame(mainFrame)
        labelFrame.grid(row=1,column=1,padx=10)
        entryFrame.grid(row=1,column=2,padx=10)
        genderFrame=Frame(entryFrame)
        genderFrame.grid(row=3,column=1)

        #Labels
        name=Label(labelFrame,text='Name',font=('Veradana 14'))
        address=Label(labelFrame,text='Address',font=('Veradana 14'))
        gender=Label(labelFrame,text='Gender',font=('Veradana 14'))
        mobileNo=Label(labelFrame,text='Mobile Number',font=('Veradana 14'))
        emailId=Label(labelFrame,text='Email-ID',font=('Veradana 14'))
        password=Label(labelFrame,text='Password',font=('Veradana 14'))

        name.grid(row=1,column=1,pady=10)
        address.grid(row=2,column=1,pady=10)
        gender.grid(row=3,column=1,pady=10)
        mobileNo.grid(row=4,column=1,pady=10)
        emailId.grid(row=5,column=1,pady=10)
        password.grid(row=6,column=1)

        #Entry
        self.nameEntry=Entry(entryFrame)
        self.addressEntry=Entry(entryFrame)
        self.var=str()
        self.maleGen=Radiobutton(genderFrame,text='Male',variable=self.var,value='M')
        self.femGen=Radiobutton(genderFrame,text='Female',variable=self.var,value='F')
        self.mobileNoEntry=Entry(entryFrame)
        self.emailIdEntry=Entry(entryFrame)
        self.passwordEntry=Entry(entryFrame)

        self.nameEntry.grid(row=1,column=1,pady=10)
        self.addressEntry.grid(row=2,column=1,pady=10)
        self.maleGen.grid(row=1,column=1,pady=10)
        self.femGen.grid(row=1,column=2,pady=10)
        self.mobileNoEntry.grid(row=4,column=1,pady=10)
        self.emailIdEntry.grid(row=5,column=1,pady=10)
        self.passwordEntry.grid(row=6,column=1)
        
        #Buttons
        self.submitBtn=Button(mainFrame,text='SUBMIT',bg='blue',fg='white',command=self.submit)
        self.submitBtn.grid(row=2,column=2)

    def openWin(self,mainFrame):
        registerWin(mainFrame)

    def returnGen(self):
        return self.var
    def submit(self):
        username=self.nameEntry.get()
        address=self.addressEntry.get()
        mobileNo=self.mobileNoEntry.get()
        gender=self.returnGen()
        emailID=self.emailIdEntry.get()
        passwd=self.passwordEntry.get()
        new_user=users.user(username,address,gender,mobileNo,emailID,passwd)
        new_user.addUserToDatabase()
        self.submitBtn.configure(text='Registered!')



'''
This Module Contains Registration Window
'''
from tkinter import *
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

        name.grid(row=1,column=1,pady=10)
        address.grid(row=2,column=1,pady=10)
        gender.grid(row=3,column=1,pady=10)
        mobileNo.grid(row=4,column=1,pady=10)
        emailId.grid(row=5,column=1,pady=10)

        #Entry
        nameEntry=Entry(entryFrame)
        addressEntry=Entry(entryFrame)
        maleGen=Radiobutton(genderFrame,text='Male',value=1)
        femGen=Radiobutton(genderFrame,text='Female',value=2)
        mobileNoEntry=Entry(entryFrame)
        emailIdEntry=Entry(entryFrame)

        nameEntry.grid(row=1,column=1,pady=10)
        addressEntry.grid(row=2,column=1,pady=10)
        maleGen.grid(row=1,column=1,pady=10)
        femGen.grid(row=1,column=2,pady=10)
        mobileNoEntry.grid(row=4,column=1,pady=10)
        emailIdEntry.grid(row=5,column=1,pady=10)
        
        #Buttons
        submitBtn=Button(mainFrame,text='SUBMIT',bg='blue',fg='white')
        submitBtn.grid(row=2,column=2)

    def openWin(self,mainFrame):
        registerWin(mainFrame)

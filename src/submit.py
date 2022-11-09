'''
This Module is for Submitting Books
'''
from tkinter import *
class submitBooks:
    def __init__(self,mainFrame):
        self.submitFrame=mainFrame
        labelContainer=Frame(self.submitFrame)
        entryFrame=Frame(self.submitFrame)
        labelContainer.grid(row=1,column=1)
        entryFrame.grid(row=1,column=2)

        #LABELS
        userName=Label(labelContainer,text='User Name',font=('Verdana 14'))
        bookName=Label(labelContainer,text='Book Name',font=('Verdana 14'))
        price=Label(labelContainer,text='Price',font=('Verdana 14'))

        userName.grid(row=1,column=1)
        bookName.grid(row=2,column=1)
        price.grid(row=3,column=1)

        #ENTRY
        userNameEntry=Entry(entryFrame)
        bookNameEntry=Entry(entryFrame)
        priceEntry=Entry(entryFrame)

        userNameEntry.grid(row=1,column=1)
        bookNameEntry.grid(row=2,column=1)
        priceEntry.grid(row=3,column=1)

        #SUBMIT 
        submitBtn=Button(self.submitFrame,text='SUBMIT',bg='blue',fg='white')
        submitBtn.grid(row=2,column=2)

    def openWin(self,mainFrame):
        submitBooks(mainFrame)

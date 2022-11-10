from tkinter import *
import tkinter
from src import login
from src import register
from src import submit

'''
Initializing root as window
'''
root=tkinter.Tk()




# Main Window
class bms:
    def __init__(self):
        root.title('Book Management System')
        self.bmsFrame = Frame(root, bg='grey', width=250, height=600)
        buttonContainer = Frame(self.bmsFrame, bg='white', width=100, height=300)
        topFrame = Frame(root, bg='grey')
        topFrame.grid(row=1, column=2)
        self.bmsFrame.grid(row=2, column=2)
        buttonContainer.pack()

        #LABELS
        welcomeMsg = Label(
            topFrame, text='BOOK MANAGEMENT SYSTEM', font=('Verdana 20'))
        welcomeMsg.pack()

        #Buttons
        loginBtn = Button(buttonContainer, bg='blue', text='Login', padx=50,command=lambda:self.bmsUserClick(0))
        registerBtn = Button(buttonContainer, bg='blue', text='New User', padx=50,command=lambda:self.bmsUserClick(1))
        availBooksBtn = Button(buttonContainer, bg='blue',
                           text='Available Books', padx=50,command=lambda:self.bmsUserClick(2))

        #Packing the Buttons
        loginBtn.grid(row=1, column=1, padx=20, pady=10)
        registerBtn.grid(row=1, column=2, padx=20, pady=10)
        availBooksBtn.grid(row=1, column=3, padx=20, pady=10)

    def clearFrame(self):
        for widget in self.bmsFrame.winfo_children():
            widget.destroy()

    def bmsUserClick(self,num):
        self.clearFrame()
        if num==0:
            root.title('Login')
            loginWindow=login.login.openWin(self,self.bmsFrame)
        elif num==1:
            root.title('Registration')
            registrationWindow=register.registerWin.openWin(self,self.bmsFrame)
            
        else:
            root.title('Submit Book')
            submitWindow=submit.submitBooks.openWin(self,self.bmsFrame)

if __name__=="__main__":
    
    openPage=bms()
    root.mainloop()
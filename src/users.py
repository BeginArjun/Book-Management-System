class user:
    def __init__(self,name,addr,gender,phNo,emailId):
        self.name=name
        self.address=addr
        self.gender=gender
        self.phNo=phNo
        self.emailId=emailId

    def userExist(self):
        '''
        If Username Exist Return True
        Else return False
        '''
        return False    #Just for now

    def addaddUserToDatabase(self,name,addr,gender,phNo,emailId):
        '''
        Adding the data to  DB with Primary Key as pHNo
        '''
        pass

    def addUser(self,name,addr,gender,phNo,emailId):
        if self.userExist()==False:
            user(name,addr,gender,phNo,emailId)
            self.addUserToDatabase(name,addr,gender,phNo,emailId)
            return True
        else:
            return False

    
    



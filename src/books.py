class books:
    def __init__(self,b_name,price,author,isin,user,qtny):
        self.isin=isin
        self.bookname=b_name
        self.price=price
        self.user=user
        self.author=author
        self.quantity=qtny

    def bookExist(self,isin):
        '''
        If Any book exist with same ISIN
        '''
        return False    #Just for now

    def addBooksToDatabase(self,b_name,price,author,isin,user,qtny):
        '''
        Add Books to Database with Primary Key as ISIN
        '''
        pass    #Just for Now

    def addBooks(self,b_name,price,author,isin,user,qtny):
        books(b_name,price,author,isin,user,qtny)
        self.addBooksToDatabase(b_name,price,author,isin,user,qtny)


    
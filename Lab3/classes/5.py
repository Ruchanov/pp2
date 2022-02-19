class Account:
    def __init__(self,owner,balance):
        self.__owner=owner
        self.__balance=balance
    
    def deposit(self,a):
        self.__balance+=a
    def get_balance(self):
        return self.__balance
    def withdraw(self,a):
        if self.__balanc>=a:
            self.__balance-=a

    
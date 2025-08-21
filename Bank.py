class Bank:
    
    def __init__(self,acc_holdername,acc_type,balance):
        self.acc_holdername=acc_holdername
        self.acc_type=acc_type
        self.__balance=balance
    
    def deposit(self,amount):
        self.__balance+=amount
        print("The account balance is ",self.__balance)
    
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance=self.__balance-amount
            print("the amount is successfully withdrawn ")
            print("the account balance is",self.__balance)
        else:
            print("Insufficient balance")

user1=Bank("jeeva","savings",1000)
user1.deposit(5000)
user1.withdraw(2000)
user2=Bank("suriya","current",200000)
user2.deposit(300000)
user2.withdraw(100000)

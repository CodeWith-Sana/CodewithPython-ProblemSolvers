class BankAccount:
    acc_num =  None
    acc_holder =  None
    balance =  None
    def __init__(self , acc_num , acc_Holder , balance):
        self.acc_num = acc_num
        self.acc_holder = acc_Holder
        self.balance = balance

    def displayFunc(self):
        print("To display User details")
        print(f"Account Number is : {self.acc_num}")
        print(f"Account Holder Name is : {self.acc_holder}")
        print(f"Account Balance  is : {self.balance}")
obj  =  BankAccount(216102 , 'Sana Salam' ,1000000.0 )
obj.displayFunc()
#to modify balance directly
setattr(obj , 'balance' , 50000)
obj.displayFunc()



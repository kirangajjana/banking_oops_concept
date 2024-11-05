import sys
class banking:
    ''' we are making an banking stimulation using opps concepts'''
    bank="Kiran Gajjana Bank"  #static variable
    branch="hyderabad" #static variable
    def __init__(self,name,balance=0.0):  #constructor
        self.name=name
        self.balance=balance
    def deposit(self,amt):  #instance method
        self.balance=self.balance+amt  #user csn add money using this method
        return self.balance
    def withdraw(self,amt): #instance method
        self.balance=self.balance-amt
        return self.balance   
    def loanservice(self,Loan): #instance method
        self.balance=self.balance+Loan #user can opt for loan upto 5lakhs more than that need further approval
user_name=input("please enter your name")   
c=banking(user_name)
while True:
    print("D-Deposit\nW-Withdrawl\nL-loan\nE-exit") #user need to select from the below options to move further
    output=input("please enter the option you want to proceed") 
    if output.lower()=="d": #checking the condition wether the person opted for deposite
            print(f"hello mr {c.name}  user welcome to the {banking.bank} of branch {banking.branch}")
            amount=int(input("enter the amount you want to deposit into your account"))
            if amount>1:
                d=c.deposit(amount)
                print(f"the updated balance in your account is {d}")
            else:
                print("please enter the valid input")    
    elif output.lower()=="w":  #checking the condition wether the person opted for withdraw
            print(f"hello  mr {c.name} user welcome to the {banking.bank} of branch {banking.branch}")
            amount=int(input("enter the amount you want to withdraw from  your account"))
            if amount<c.balance:
                d=c.withdraw(amount)
                print(f"the total amount you have withdrawn {d}")
            else:
                print("sorry you dont have the balance to go with the above transaction")
                sys.exit()

    elif output.lower()=="l":
            print(f"hello mr {c.name} user welcome to the {banking.bank} of branch {banking.branch}")
            amount=int(input("enter the amount you want to take loan from the bank"))
            print(f"the amount you have taken the loan from banlk is {amount}")
            c.balance=c.balance+amount
            print(f"the updated amount in your acount is {c.balance}")


            



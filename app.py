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
print("D-Deposit\nW-Withdrawl\nL-loan\nE-exit") #user need to select from the below options to move further
output=input("please enter the option you want to proceed") 
while True:
    if output.lower()=="d":
        print(f"hello user welcome to the {banking.bank} of branch {banking.branch}")
        print("enter the amount you want to deposit into your account")

class banking:
    ''' we are making an banking stimulation using opps concepts'''
    bank="Kiran Gajjana Bank"  #static variable
    branch="hyderabad" #static variable
    def __init__(self,name,balance=0.0):  #constructor
        self.name=name
        self.balance=balance
    def deposit(self,amt):  #instance method
        self.balance=self.balance+amt  #user csn add money using this method



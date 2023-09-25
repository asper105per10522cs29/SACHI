#transaction details class bankacccount:

def __init__(self,account_number,account_holder_name,account_balance=0): self.account number-account_number

self.account holder_name=account_holder_name

self.account balance-account_balance

def deposit money(self,amount):

if amount>0:

self.account balance +=amount print("the credit amount is: (0) and your current balance is:

(1).format(amount,self.account balance))

else:

print("please enter the amount")

def withdraw money(self,amount):

if amount>0 and self.account balance>=amount:

self.account_balance-=amount

print("debited amount is: (0) and your currnet balance is:

(1).format(amount,self.account balance))

else:

print('insufficient balance)

def display balance(self):

print("the account number:(0)'s current balance is: (1).format(self.account number,self.account balance)) result-bankacccount(account_number=10001,account_holder_name='sakthivel',

account_balance=10000)

result.withdraw_money(2000) result.deposit money(3000)

result.display_balance()
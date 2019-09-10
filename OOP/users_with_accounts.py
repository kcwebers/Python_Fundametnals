class BankAccount:		
    def __init__(self, account_balance, account_interest):
        self.account_balance = account_balance
        self.account_interest = account_interest
    def deposit(self, amount):	
        self.account_balance += amount
        return self
    def withdrawal(self, amount):  # decreases the account balance by the given amount if there are sufficient funds;
        if self.account_balance >= amount:  #  if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
            self.account_balance -= amount 
            return self 
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
            return self
    def display_account_info(self):     # have this method print the account balance
        print(f"Balance: ${self.account_balance}")
        return self
    def yield_interest(self):   # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.account_balance > 0:
            self.account_balance = self.account_balance + (self.account_balance * self.account_interest)
            return self

class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(account_balance, account_interest)
    def make_deposit(self, amount):	
    	self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):  # have this method decrease the user's balance by the amount specified
        self.account.withdrawal(amount) 
        return self  
    def display_user_balance(self):     # have this method print the user's name and account balance to the terminal
        print(f"User: {self.name}, Balance: ${self.account.display_account_info}")
        return self
    def transfer_money(self, other_user, amount):       #have this method decrease the user's balance by the amount and add that amount to other other_user's balance
        self.account -= amount  
        other_user.account += amount
        return self







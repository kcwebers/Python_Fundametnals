class BankAccount:		
    def __init__(self, account_balance, account_interest):
        if ac
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

firstAccount = BankAccount(100000, 0.03)
secondAccount = BankAccount(500, 0.05)

firstAccount.deposit(500).deposit(1000).deposit(75).withdrawal(1500).yield_interest().display_account_info()

secondAccount.deposit(50).deposit(500).withdrawal(50).withdrawal(25).withdrawal(25).withdrawal(25).yield_interest().display_account_info()





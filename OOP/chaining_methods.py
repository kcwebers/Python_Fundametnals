class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        self
    def make_deposit(self, amount):	
    	self.account_balance += amount
        return self
    def make_withdrawal(self, amount):  # have this method decrease the user's balance by the amount specified
        self.account_balance -= amount 
        return self  
    def display_user_balance(self):     # have this method print the user's name and account balance to the terminal
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):       #have this method decrease the user's balance by the amount and add that amount to other other_user's balance
        self.account_balance -= amount  
        other_user.account_balance += amount
        return self

molly = User("Molly Ann Marie", "mollyann@yahoo.com")
jeremy = User("Jeremy Toodles", "jtoodles@gmail.com")
chuck = User("Chuck Willis", "chuckster23@hotmail.com")

molly.make_deposit(50).make_deposit(100).make_deposit(1000000).make_withdrawal(45).display_user_balance()

jeremy.make_deposit(250).make_deposit(450).make_withdrawal(25).make_withdrawal(75).display_user_balance()

chuck.make_deposit(750).make_withdrawal(50).make_withdrawal(50).make_withdrawal(700).display_user_balance()

molly.transfer_money(chuck, 50000).display_user_balance()

chuck.display_user_balance()


# make sure to return self!!


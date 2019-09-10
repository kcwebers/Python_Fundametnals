class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):	
    	self.account_balance += amount
    def make_withdrawal(self, amount):  # have this method decrease the user's balance by the amount specified
        self.account_balance -= amount   
    def display_user_balance(self):     # have this method print the user's name and account balance to the terminal
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    def transfer_money(self, other_user, amount):       #have this method decrease the user's balance by the amount and add that amount to other other_user's balance
        self.account_balance -= amount  
        other_user.account_balance += amount

molly = User("Molly Ann Marie", "mollyann@yahoo.com")
jeremy = User("Jeremy Toodles", "jtoodles@gmail.com")
chuck = User("Chuck Willis", "chuckster23@hotmail.com")

molly.make_deposit(50)
molly.make_deposit(100)
molly.make_deposit(1000000)
molly.make_withdrawal(45)
molly.display_user_balance()

jeremy.make_deposit(250)
jeremy.make_deposit(450)
jeremy.make_withdrawal(25)
jeremy.make_withdrawal(75)
jeremy.display_user_balance()

chuck.make_deposit(750)
chuck.make_withdrawal(50)
chuck.make_withdrawal(50)
chuck.make_withdrawal(700)
chuck.display_user_balance()

molly.transfer_money(chuck, 50000)
molly.display_user_balance()
chuck.display_user_balance()



class User:
    pass    # we'll fill this in shortly

michael = User()
anna = User()

# The first parameter of every method within a class will be self, and the class's attribute names are also indicated by self.. 
# We'll talk more about self later, but for now just follow this pattern: self.<<attribute_name_of_your_choosing>>.

class User:		# declare a class and give it name User
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

guido = User()
monty = User()

print(guido.name)	# output: Michael
print(monty.name)	# output: Michael

# this is like assigning overriding variables in python/JS; the variable name doesn't matter if it is consistently assigned same value

guido.name = "Guido"
monty.name = "Monty"

# While we definitely want every user to have a name, email, and account balance, we don't want all of our users to have 
# the same name and email address upon creation. How will we know what the name should be?

# With the __init__ method's parameters, we indicate what needs to be provided (i.e. arguments) when the class is instantiated. 
# (self is always passed in implicitly.)

# In our example, even though we have 3 attributes, we only require input for 2 of them. When the User instance is created, 
# we should expect to receive specific values for the name and email address. We'll assume, however, that everyone starts with 
# $0 in their account. Let's adjust our code to allow arguments to be passed in upon instantiation:

class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter

guido = User("Guido van Rossum", "guido@python.com") # since the first parameter (self) is implicit, can be omitted on the call?
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python


# Now it's time to add some functionality to our class. Methods are just functions that belong to a class. This means that we can't 
# call them independently as we have called functions previously; rather, methods must be called from an instance of a class. 
# For example, if a user wanted to make a deposit, we'd want to be able to call the method from the user instance; because a specific 
# user is making a deposit, it should only affect that user's balance. Making such a call would look something like this:

guido.make_deposit(100)

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

# Don't forget that the first parameter of every method within a class should be self. Notice that, in addition to whatever arguments
# are passed in as a traditional function, methods also have access to the class's attributes.

# after method has been written/implemented into user, it can be called

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50

# It's probably time to talk about self. The self parameter includes all the information about the individual object that 
# has called the method. But how does it get passed in? Based on the signature for the deposit method or the __init__ method, 
# they require 2 and 3 arguments, respectively. However, when we call on them, we pass in only 1 and 2. What's happening here? 
# Because we are calling on the method from the instance, this is known as implicit passage of self. When we call on a method from an 
# instance, that instance, along with all of its information (name, email, balance), is passed in as self.

# Modules & Packages

# Creating Your Own Modules
# Writing your own Python modules is very simple. To create a module, we first create a new .py file with the module name in the same 
# directory as the file that will import the module. Then we import it using the import command and the Python file name (without the .py extension)

# For example, let's create a module of arithmetic operations:

# modular_example/arithmetic.py

def add(x, y):
    return x + y
def multiply(x, y):
    return x * y
def subtract(x, y):
    return x - y

# Now, make another file in the same directory as arithmetic.py called calculations.py. We can import the arithmetic module into 
# calculations.py and run the functions by doing this...

# modular_example/calculations.py

import arithmetic
print(arithmetic.add(5, 8))
print(arithmetic.subtract(10, 5))
print(arithmetic.multiply(12, 6))

# Note: make sure that the module and the file importing the module are in the same folder/directory.




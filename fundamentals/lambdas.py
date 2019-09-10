# Another type of function mentioned earlier is the anonymous function. Simply put, an anonymous function is a function without a name. 
# In Python, anonymous functions are created with the lambda keyword. These functions are used for various purposes:

# they are handy in situations where we only need to use the function once
# they are lightweight when we need to break down complex tasks into small, specific tasks
# they are convenient as arguments to functions that require functions as parameters
# Earlier, we defined the square() function that takes in one parameter (num), squares it and then returns it:

def square(num):
    x = num ** 2
    return x

# Now we can rewrite this function as an anonymous (nameless) lambda function:

lambda num: num ** 2

# What if you wanted to create an anonymous (nameless) function that takes two arguments and returns the sum of the two arguments?

lambda num1, num2: num1+num2

# A lambda could be:

        # an element in a list:

# create a new list, with a lambda as an element
my_list = ['test_string', 99, lambda x : x ** 2]
# access the value in the list
print(my_list[2]) # will print a lambda object stored in memory
# invoke the lambda function, passing in 5 as the argument
my_list[2](5)

        # passed to another function as a callback:
# define a function that takes one input that is a function
def invoker(callback):
    # invoke the input pass the argument 2
    print(callback(2))
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

        # stored in a variable:
add10 = lambda x: x + 10 # store lambda expression in a variable
add10(2)  # returns 12
add10(98) # returns 108

        # returned by another function:
def incrementor(num):
    start = num
    return lambda x: num + x

# lambdas are great for single use functions! if soemthing is used only once we can pass in a lambdas instead of generating a full definition


# instead of this
        my_arr = [1,2,3,4,5]
        # define a function that squares values
        def square(num):
            return num ** 2
        # invoke map function
        print(list(map(square, my_arr)))
# try this
        my_arr = [1,2,3,4,5]
        print(list(map(lambda x: x ** 2, my_arr))) # invoke map, pass in a lambda as the first argument

# map()
# reduce()
# sort() - lambda is optional
# filter()



# A ternary operator, or conditional expression, is an operator that takes 3 arguments. Most simply, they are a one line if-else statement. 
# In many languages, we see this same functionality with the symbols ? and :. In Python, the syntax is as follows:

# <result_if_true> if <condition> else <result_if_false>
# If you've seen this operator in any other languages, Python's syntax can feel awkward, but with practice it will become easier to use 
# and read. And don't forget that we can always use the traditional if-else statement instead.

# Here's an example:

# traditional
if stacks >= 3:
    print('Coding Dojo')
else:
    print('You are not Coding Dojo!')
# ternary
print('Coding Dojo' if stacks >= 3 else 'You are not Coding Dojo!')

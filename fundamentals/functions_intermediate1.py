import random
def randInt(min=0, max=100):
    if max < min:
        num = random.random() * (min - max) + max   #assumed that we still want a number b/w the two givens, regardless of which is higher
        return round(num)                           #per : If both a min and max number are provided, the function should return a random integer between those 2 values.
    num = random.random() * (max - min) + min
    return round(num)

#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

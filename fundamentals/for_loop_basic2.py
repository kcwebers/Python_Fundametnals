# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggieSize(li):
    for x in range(len(li)):
        if li[x] > 0:
            li[x] = "big"
    return li

# print(biggieSize([-1, 3, 5, -5])) = [-1, "big", "big", -5]


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def countPositives(li):
    count = 0
    for x in li:
        if x >= 0:
            count += 1
    li[len(li) - 1] = count
    return li

# countPositives([1,6,-4,-2,-7,-2]) = [1,6,-4,-2,-7,2]

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sumTotal(li):
    added = 0
    for x in li:
        added += x
    return added

# sumTotal([6,3,-2]) = 7

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def average(li):
    added = 0
    for x in li:
        added += x
    return added / len(li)

# average([1,2,3,4]) = 2.5

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(li):
    return len(li)

# length([37,2,1,-9]) = 4

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(li):
    min = li[0]
    if len(li) == 0:
        return False
    for x in li:
        if x < min:
            min = x
    return min

#  minimum([37,2,1,-9]) = -9

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(li):
    max = li[0]
    if len(li) == 0:
        return False
    for x in li:
        if x > max:
            max = x
    return max   

# maximum([37,2,1,-9]) = 37

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimateAnalysis(li):
    newDict = {'sumTotal': 0, 'average': 7.75, 'min': li[0], 'max': li[0], 'length': len(li)}
    for x in li:
        if x > newDict['max']:
            newDict['max'] = x
            newDict['sumTotal'] += 1
        elif x < newDict['min']:
            newDict['min'] = x
            newDict['sumTotal'] += 1
    return newDict

ultimateAnalysis([37,2,1,-9])

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. 
# (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverseList(li):
    for x in range(0, len(li)//2):
        tmp = li[x]
        li[x] = li[len(li)-x-1]
        li[len(li)-x-1] = tmp
    return li

reverseList([37,2,1,-9])

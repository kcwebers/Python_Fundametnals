# Update Values in Dictionaries and Lists
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def swapEm(li):
    for i in range(len(li)):
        for k in range(len(li[i])):
            if li[i][k] == 10:
                li[i][k] = 15
    return li

print(swapEm(x))

def changeEm(li):
    for x in range(len(li)):
        for value in li[x]:
            if li[x][value] == 'Jordan':
                li[x][value] = 'Bryant'
    return li

print(changeEm(students))

def changeEmAgain(li):
    for x in li:
        for y in range(len(li[x])):
            if li[x][y] == 'Messi':
                li[x][y] = 'Andres'
    return li

print(changeEmAgain(sports_directory))


def changeZ(arr):
    for x in range(len(arr)):
        for value in arr[x]:
            if arr[x][value] == 20:
                arr[x][value] = 30
    return z

print(changeZ(z))


# Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function 
# loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}, 
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for x in range(len(some_list)):
        print(some_list[x])

iterateDictionary(students)

# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function 
# prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        print(some_list[x][key_name])

iterateDictionary2('first_name', students)

# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with 
# the size of its list, and then prints the associated values within each key's list. For example:

def printInfo(some_dict):
    for x in some_dict:
        count = 0
        for y in range(len(some_dict[x])):
            count += 1
        print(count, x)
        for y in range(len(some_dict[x])):
            print(some_dict[x][y])

print(printInfo(dojo))


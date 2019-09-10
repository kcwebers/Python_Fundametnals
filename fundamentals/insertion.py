# Build an algorithm for insertion sort. Please watch the video here to understand how insertion sort works and implement the code. 
# Basically, this sort works by starting at index 1, shifting that value to the left until it is sorted relative to all values to the 
# left, and then moving on to the next index position and performing the same shifts until the end of the list is reached. The following 
# animation also shows how insertion sort is done.

# Some Tips!
# Don't forget to write your plan in a non-programming language first (pseudocode!) and test your base cases before you build your code.

# Please refrain from checking other people's code. If your code does NOT work as intended make sure

# you are writing up your plan first,
# your plan solves your base case, and
# your plan solves other base cases you have specified.
# Sometimes if you are stuck for too long, you need to just start all over as this can be more efficient to do than dwelling on old code 
# with bugs that are hard to trace.

def insertionSort(li):
    for x in range(len(li)):    # loop through initial list to access each element
        for y in range(x + 1, len(li)):  # loop through same array starting at index +1 ahead of x
            if(li[x] > li[y]):   # if element (li[y]) is greater than the one before it (li[x], which is set to be one index behind always)
                tmp = li[x]      # swap the smaller element with the with the original element
                li[x] = li[y]
                li[y] = tmp 
    return li                    # return final array

# this is the answer per online looking ... I think I am a bit confused about what an insertion sort is
def insertionSort(li): 
    for i in range(1, len(li)): # loop through array starting at the first index
        key = li[i] 
        j = i - 1 # Move elements that are greater than key to one position ahead of their current position 
        while j >= 0 and key < li[j] : 
                li[j + 1] = li[j] 
                j -= 1
        li[j + 1] = key

print(insertionSort(arr))
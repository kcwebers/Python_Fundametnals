# If you're given a list with a bunch of numbers and you're supposed to sort the numbers (with the smallest number on the left 
# and the largest number on the right), how would you do this? There are numerous sorting algorithms to sort numbers in the list. 
# We'll introduce one of the simplest sorting algorithm called selection sort.

# Selection sort works by iterating through the list, finding the minimum value, and moving it to the beginning of the list. Then, 
# ignoring the first position, which is now sorted, iterate through the list again to find the next minimum value and move it to index 1. 
# This continues until all values are sorted. Here's an animation and a video of selection sort:

def selectionSort(li):
    for x in range(len(li)):    # loop through initial list to access each element
        minIndex = x            # set the minimum index to the index at use
        for y in range(x + 1, len(li)):     # loop through array again, starting at the +1 index
            if li[minIndex] > li[y]:        # compare the item at the original index with all proceding
              minIndex = y                  # if proceding item at idex is less than item at minIdex, set to minIndex
        tmp = li[x]              # swap the found element with the with the original element
        li[x] = li[minIndex]
        li[minIndex] = tmp       # loop with go through again for each element in array
    return li                    # return final array

print(selectionSort(arr))
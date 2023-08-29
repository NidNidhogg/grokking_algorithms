# Arrays and related elements
# Element position = index
#There are two types of access: random and sequential

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print (selectionSort( [5, 3, 6, 2, 10] ))


# The computer's memory is like a huge cabinet with drawers.
# Lists provide fast insertion and execution.
# In an array, all elements are stored in memory next to each other.
# In a list, elements are scattered in random memory locations, and each element stores the address of the next element.
# Arrays provide fast reading.
# All elements of an array must be of the same type (only integers,
# only floating-point numbers, etc.).
# If you need to store a set of elements, use an array or a list.

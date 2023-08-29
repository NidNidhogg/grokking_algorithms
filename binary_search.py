# In binary search, half of the numbers are excluded each time.
# Logarithm is the operation that is the inverse of exponentiation.
# 2**5 = 32 <-> log2(32) = 5
# Binary search only works if the list is sorted.

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))

# O describes how fast an algorithm works.
# O(n) - simple search/linear time; O(log n) - binary search/logarithmic time where n is the number of operations.

# The speed of algorithms is measured not in seconds but in the rate of growth of the number of operations.



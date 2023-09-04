#Is it possible to solve this problem using the 'divide and conquer' strategy?

#The solution of the problem using the 'divide and conquer' method consists of two steps: 
#1. First, the base case is defined. This should be the simplest case among all possible ones. 
#2. The problem is divided or reduced until it is reduced to the base case.

def sum(arr):
    total = 0
    for x in arr:
        total +=x
    return total

print (sum([1,2,3,4,5]))

#Advice: When you write a recursive function involving an array, the base case often turns out to be an empty array or an array with one element. 
#If you're not sure where to start, start with this.


def count_elements(lst):
    # Base case: if the list is empty, return 0
    if not lst:
        return 0
    
    else:
        # Recursive case: count the first element and recurse on the rest of the list
        return 1 + count_elements(lst[1:])

# Example usage:
my_list = [1, 2, 3, 4, 5]
count = count_elements(my_list)
print("The number of elements in the list is:", count)


#The quicksort algorithm works as follows: first, an element is selected in the array, which is called the pivot.

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))

#If you implement the quicksort algorithm, choose a random element as the pivot. The average runtime of quicksort is O(n log n)!
#Constants in 'big O' notation sometimes matter. This is why quicksort is faster than merge sort.
#When comparing simple sorting to binary, the constant almost never matters because O(log n) greatly outperforms O(n) in speed for large list sizes.
#Recursion is a fundamental programming concept where a function calls itself in order to solve a problem
#Every recursive function consists of two parts: the base case and the recursive case


# Input a number from the user
n = int(input("Enter a non-negative integer: "))

def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Call the factorial function with the user's input and print the result
result = factorial(n)
print(f"The factorial of {n} is {result}")

#A function call stack or simply a stack. 
#The stack is a data structure that operates on the principle of "last-in, first-out" (LIFO).

#The call stack plays a vital role in recursion. 
#When a function calls itself in a recursive call, each new call creates a new entry on the stack. 
# These entries are stored and retrieved in LIFO order, allowing recursive functions to work correctly.

#The stack supports two operations: push and pop of elements.
#All function calls are stored in the call stack.
#If the call stack becomes very large, it will consume too much memory.
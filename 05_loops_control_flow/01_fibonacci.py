# Constant for the maximum value in the Fibonacci sequence
MAX_VALUE = 10000

# Initial terms of the Fibonacci sequence
fib0, fib1 = 0, 1

# Print the initial term
print(fib0, end=" ")

# Continue generating terms as long as they are less than MAX_VALUE
while fib1 < MAX_VALUE:
    print(fib1, end=" ")
    fib0, fib1 = fib1, fib0 + fib1  # Update terms to the next in the sequence

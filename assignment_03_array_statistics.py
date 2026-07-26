# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def calculate_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

def calculate_average(arr):
    total = calculate_sum(arr)
    return total / len(arr)

def find_maximum(arr):
    highest = arr[0]
    for num in arr:
        if num > highest:
            highest = num
    return highest

def find_minimum(arr):
    lowest = arr[0]
    for num in arr:
        if num < lowest:
            lowest = num
    return lowest

# ==========================================
# Main block
# ==========================================
n = int(input("How many numbers? "))

if n <= 0:
    print("Error: Number of elements must be a positive integer.")
else:
    numbers = []
    
    # Loop to collect user input
    for i in range(1, n + 1):
        val = float(input(f"Enter number {i}: "))
        # Formatting to keep the output clean (removes .0 from whole numbers)
        if val.is_integer():
            val = int(val)
        numbers.append(val)
    
    # Output the calculated results
    print("\nResults:")
    print(f"Sum:     {calculate_sum(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Maximum: {find_maximum(numbers)}")
    print(f"Minimum: {find_minimum(numbers)}")

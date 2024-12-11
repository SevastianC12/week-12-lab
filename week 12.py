#Design a recursive function that accepts an integer argument, n, , and prints the numbers 1 up through n
def print_numbers(n):
    # Base case: when n is 0 or less, stop the recursion
    if n <= 0:
        return
    # Recursive case: print numbers up to n-1 and then print n
    print_numbers(n - 1)
    print(n)

# Example usage:
print_numbers(5)


#Design a recursive function that accepts two arguments into the parameters x and y.
def main():
    #Get two numbers.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    #Display their product. 
    print('Their product is' , multiply(num1, num2))
def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    else: 
        return x + multiply (x, y-1)
    
# call the main function.
main()


#Write a recursive function that accepts an integer argument n. 
def print_asterisks(n, current=1):
    # Base case: if current exceeds n, stop recursion
    if current > n:
        return
    
    # Print the current number of asterisks
    print('*' * current)
    
    # Recursively call the function for the next line
    print_asterisks(n, current + 1)

# Example usage:
n = 5
print_asterisks(n)


#Design a function that accepts a list as an argument and returns the largest value in the list. The function should use recursion to find the largest item.
def find_largest(lst):
    # Base case: if the list has only one element, return it
    if len(lst) == 1:
        return lst[0]
    
    # Recursive case: compare the first element with the largest of the rest of the list
    largest_of_rest = find_largest(lst[1:])
    
    # Return the larger of the first element or the largest of the rest of the list
    if lst[0] > largest_of_rest:
        return lst[0]
    else:
        return largest_of_rest

# Example usage:
lst = [3, 5, 7, 2, 8, 1]
print(find_largest(lst))


#Design a function that accepts a list of numbers as an argument. The function should recursively calculate the sum of all the numbers in the list and return that value.
def recursive_sum(numbers):
    # Base case: if the list is empty, return 0
    if not numbers:
        return 0
    # Recursive case: sum the first element with the sum of the rest of the list
    return numbers[0] + recursive_sum(numbers[1:])

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = recursive_sum(numbers)
print(result)  # Output: 15



#Design a function that accepts an integer argument and returns the sum of all the integers from 1 up to number passed as an argument.
def sum_of_integers(n):
    # Base case: when n is 1, return 1
    if n == 1:
        return 1
    # Recursive case: sum of n + sum of integers from 1 to n-1
    else:
        return n + sum_of_integers(n - 1)

# Example usage:
result = sum_of_integers(50)
print(result)  # Output: 1275


#Design a function that uses recursion to raise a number to a power. The function should accept two arguments: the number to be raised, and the exponent. Assume the exponent is a nonnegative integer.
def power(base, exponent):
    # Base case: any number raised to the power of 0 is 1
    if exponent == 0:
        return 1
    # Recursive case: base raised to the power of exponent is base * base^(exponent - 1)
    else:
        return base * power(base, exponent - 1)

# Example usage:
result = power(2, 5)
print(result)  # Output: 32


#Designa function ackermann(m, n), which solves ackermann's function.
def Ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return Ackermann(m - 1, 1)
    else:
        return Ackermann(m - 1, Ackermann(m, n - 1))

# Example usage:
result = Ackermann(3, 4)
print(result)

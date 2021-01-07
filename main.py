# Eric Reece
# 1/6/2021
# This python project is designed to test a variety of recursive implementations.
# First, calculates the sum of digits. Then, gets the power of x to y.


# Function to calculate the sum of a given integers' individual members
def sum_digits(user_value):
    if user_value == 0:
        return 0
    else:
        return user_value % 10 + sum_digits(int(user_value / 10))


# Function to obtain the value of 'x' to power 'y'
def get_power(x, y):
    if y == 0:
        return 1
    elif x == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x * get_power(x, y - 1)


# Function to calculate the greatest common divisor of a pair of integers.
def gcd(value1, value2):
    low = min(value1, value2)
    high = max(value1, value2)

    if low == 0:
        return high
    elif low == 1:
        return 1
    else:
        return gcd(low, high % low)


# Function to calculate positive integers of n+(n-2)+(n-4)... (until n-x =< 0)
def sum_series(value):
    if value < 1:
        return 0
    else:
        return value + sum_series(value - 2)


# Function to calculate the factorial of user input
def factorial(value):
    if value == 0:
        return 0
    elif value == 1:
        return value
    else:
        return value * factorial(value)


if __name__ == '__main__':

    user_selection = int(input("Welcome to the recursion program. Pick from the following list to test a function:\n"
                               "1: Sum of integers\n"
                               "2: Power function\n"
                               "3: Greatest Common Divisor\n"
                               "4: Sum Series function\n"
                               "5: Factorial function\nUser Selection: "))

    if user_selection == 1:
        print("*** Recursion 1: Sum of integers ***\n")
        user_sum = int(input("Enter a non-negative number to sum its members: "))
        print(sum_digits(user_sum))
    elif user_selection == 2:
        print("*** Recursion 2: Power function ***\n")
        user_base = int(input("Enter a base: "))
        user_power = int(input("Enter a power: "))
        print(str(user_base) + " to the power of " + str(user_power) + " is: " + str(get_power(user_base, user_power)))
    elif user_selection == 3:
        print("*** Recursion 3: Greatest Common Divisor ***\n")
        user_num1 = int(input("Enter value 1: "))
        user_num2 = int(input("Enter value 2: "))
        print(gcd(user_num1, user_num2))
    elif user_selection == 4:
        print("*** Recursion 4: Sum Series ***\n")
        series_input = float(input("Enter a value to find the sum series: "))
        print(sum_series(series_input))
    elif user_selection == 5:
        print("*** Recursion 5: Factorials ***\n")
        user_factorial = int(input("Enter a number to test the factorial function: "))
        print(factorial(user_factorial))



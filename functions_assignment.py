# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    print(f"hello_{user_name}! - functions_assignment.py:4")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for number in range(1, 101):
        if number % 2 != 0:
            print(number)

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    if not a_list:
        return None
    return max(a_list)

# Question 4
# Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
def is_leap_year(a_year):
    return (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0)

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# The return should be boolean Type.
def is_consecutive(a_list):
    if not a_list:
        return False
    sorted_list = sorted(a_list)
    return all(sorted_list[i] + 1 == sorted_list[i + 1] for i in range(len(sorted_list) - 1))

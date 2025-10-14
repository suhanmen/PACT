"""
Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
assert check_expression("{()}[{}]") == True
"""


import re

def check_expression(expression):
    # Using a stack to keep track of opening brackets
    stack = []
    # Dictionary to hold matching pairs
    brackets = {'(': ')', '{': '}', '[': ']'}

    # Iterate over each character in the expression
    for char in expression:
        # If the character is an opening bracket, push to stack
        if char in brackets:
            stack.append(char)
        # If the character is a closing bracket
        elif char in brackets.values():
            # If stack is empty or doesn't match the corresponding opening bracket, return False
            if not stack or char != brackets[stack.pop()]:
                return False

    # If stack is not empty at the end, return False, otherwise True
    return not stack

# Test the function
assert check_expression("{()}[{}]") == True

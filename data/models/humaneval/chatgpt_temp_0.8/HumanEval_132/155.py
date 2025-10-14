def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''

    stack = [] # Create an empty list to act as a stack

    # Iterate over each bracket in the string
    for bracket in string:
        if bracket == '[':
            stack.append(bracket) # If the bracket is an opening bracket, add it to the stack
        elif bracket == ']':
            if not stack: # If there are no opening brackets in the stack, return False
                return False
            stack.pop() # If the bracket is a closing bracket, remove the top opening bracket from the stack

    # If there are no opening brackets left in the stack, return False
    return False if stack else True

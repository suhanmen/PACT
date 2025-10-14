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

    # Create a stack to keep track of opening brackets
    stack = []

    # Iterate through each bracket in the string
    for bracket in string:

        # If the bracket is an opening bracket, add it to the stack
        if bracket == '[':
            stack.append(bracket)

        # If the bracket is a closing bracket, check if there is a matching opening bracket in the stack
        elif bracket == ']':
            if len(stack) > 0 and stack[-1] == '[':
                # If there is a matching opening bracket, remove it from the stack
                stack.pop()
            else:
                # If there is no matching opening bracket, return False
                return False

    # If there are any opening brackets left in the stack, return True (since at least one bracket must be nested)
    return len(stack) > 0

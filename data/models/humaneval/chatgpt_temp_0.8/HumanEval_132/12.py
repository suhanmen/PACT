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
    stack = []
    for char in string:
        if char == "]" and stack and stack[-1] == "[":
            # Remove the last open bracket from the stack
            stack.pop()
            # Check if the sequence is nested
            if len(stack) > 0:
                return True
        else:
            # Add the current bracket to the stack
            stack.append(char)
    return False

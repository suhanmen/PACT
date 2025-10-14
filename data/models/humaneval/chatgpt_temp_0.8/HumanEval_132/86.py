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

    # If the length of the string is odd, it means there can't be any nested brackets
    if len(string) % 2 == 1:
        return False

    stack = []

    # Iterate through the string
    for char in string:
        if char == '[':
            # Push the opening bracket onto the stack
            stack.append(char)
        else:
            # If the stack is empty or the top of the stack is not an opening bracket, return False
            if len(stack) == 0 or stack[-1] != '[':
                return False
            # Otherwise, pop the opening bracket from the stack
            stack.pop()

    # If the stack is empty, there were no nested brackets
    if len(stack) == 0:
        return False

    return True

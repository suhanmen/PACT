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
    # Use a stack to keep track of opening brackets
    stack = []
    
    # Iterate through each bracket in the string
    for bracket in string:
        if bracket == '[':
            # If we see an opening bracket, we push it onto the stack
            stack.append(bracket)
        elif bracket == ']':
            # If we see a closing bracket, we check if the top of the stack is an opening bracket
            if len(stack) > 0 and stack[-1] == '[':
                # If it is, we pop the opening bracket off the stack
                stack.pop()
            else:
                # If it's not, the brackets are not nested so we can return False
                continue
    
    # If the stack is empty, then there must have been a valid subsequence of nested brackets
    return len(stack) == 0 or len(stack) < len(string)

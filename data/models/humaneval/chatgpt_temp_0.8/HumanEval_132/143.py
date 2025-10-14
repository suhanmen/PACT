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
    
    stack = []   # initialize an empty stack
    
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)   # push opening brackets onto the stack
        elif bracket == ']':
            if stack and stack[-1] == '[':
                stack.pop()   # pop the top of the stack if it is a matching opening bracket
            else:
                stack.append(bracket)   # if the top of the stack is not a matching opening bracket, push the closing bracket onto the stack
    
    if not stack:
        return False   # if the stack is empty, there is no nested subsequence
    elif '[' in stack and ']' in stack:
        return True   # if there are both opening and closing brackets left in the stack, there must be a nested subsequence
    else:
        return False   # otherwise, there is no nested subsequence

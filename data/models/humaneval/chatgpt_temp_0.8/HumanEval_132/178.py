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
    if '[]' not in string:
        return False
    if string.count('[') != string.count(']'):
        return False
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append('[')
        elif bracket == ']':
            if not stack:
                return False
            stack.pop()
            if not stack:
                return True
    return False

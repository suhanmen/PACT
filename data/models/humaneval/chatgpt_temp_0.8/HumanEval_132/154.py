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

    opening_brackets = []
    for bracket in string:
        if bracket == '[':
            opening_brackets.append(bracket)
        elif bracket == ']':
            if len(opening_brackets) == 0:
                continue
            opening_brackets.pop()
            if len(opening_brackets) > 0:
                return True

    return False

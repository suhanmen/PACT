from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # remove any spaces in the input string
    paren_string = paren_string.replace(' ', '')
    # initialize a stack to keep track of opening parentheses
    stack = []
    # initialize variables for the start and end indices of each group
    start_index = 0
    end_index = 0
    # initialize a list to store the separate groups
    groups = []
    # iterate through the input string
    for i in range(len(paren_string)):
        # if we encounter an opening parenthesis, add its index to the stack
        if paren_string[i] == '(':
            stack.append(i)
        # if we encounter a closing parenthesis, pop the last opening parenthesis index from the stack
        # if the stack is empty, we have found the end of a group
        elif paren_string[i] == ')':
            if stack:
                stack.pop()
            else:
                end_index = i
                groups.append(paren_string[start_index:end_index+1])
                start_index = i+1
    # add the final group 

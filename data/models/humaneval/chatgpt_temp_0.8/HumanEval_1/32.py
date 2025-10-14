from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '')  # remove any spaces in the input string
    result = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            j = i + 1
            count = 1
            while count != 0:
                if paren_string[j] == '(':
                    count += 1
                elif paren_string[j] == ')':
                    count -= 1
                j += 1
            result.append(paren_string[i:j])
            i = j
        else:
            i += 1
    return result

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if is_palindrome(string):  # if the string is already a palindrome
        return string
    
    for i in range(len(string)-1, -1, -1):  # iterate over possible palindromic suffixes
        if is_palindrome(string[i:]):  # if the suffix is a palindrome
            prefix = string[:i]  # get the prefix that comes before the suffix
            return string + prefix[::-1]  # append the reversed prefix to the string to get the palindrome

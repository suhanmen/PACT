def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if is_palindrome(string):
        # if input string is already a palindrome, return it
        return string
    for i in range(len(string)-1, -1, -1):
        # iterate over the string in reverse order
        if is_palindrome(string[i:]):
            # if a palindromic suffix is found, append the reverse of the prefix to it and return
            return string + string[:i][::-1]

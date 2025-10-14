def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if not string:
        # empty string is already a palindrome
        return ''

    for i in range(len(string), 0, -1):
        # check if the postfix is a palindrome
        if is_palindrome(string[-i:]):
            # get the prefix that comes before the palindrome
            prefix = string[:-i]
            # append the reverse of the prefix to the string
            return string + prefix[::-1]

    # if no palindromic postfix was found, the whole string is a palindrome
    return string

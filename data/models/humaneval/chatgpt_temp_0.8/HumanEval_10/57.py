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
        # if the string is already a palindrome, return it
        return string
    
    # find the longest palindromic suffix of the input string
    for i in range(len(string)-1, -1, -1):
        if is_palindrome(string[i:]):
            # we have found the longest palindromic suffix
            # now we need to find the prefix that comes before it
            prefix = string[:i]
            # append the reverse of the prefix to the end of the string
            return string + prefix[::-1]
    
    # if we reach this point, the input string had no palindromic suffix
    # in this case, we just need to append the reverse of the whole string to itself
    return string

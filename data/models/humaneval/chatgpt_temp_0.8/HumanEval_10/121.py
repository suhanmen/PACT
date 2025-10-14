def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if is_palindrome(string):  # if the string is already a palindrome, no need to add anything
        return string

    for i in range(len(string), 0, -1):  # start from the end of the string and work backwards
        if is_palindrome(string[i-1:]):  # check if the current postfix is a palindrome
            prefix = string[:i-1]  # get the prefix before the palindromic suffix
            return string + prefix[::-1]  # append the reversed prefix to the end of the string to form a palindrome

    # if we reach this point then we couldn't find a palindromic postfix, so just return the reversed string
    return string[::-1]

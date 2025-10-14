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
    else:
        # find the longest palindromic suffix of the string
        for i in range(len(string)-1, -1, -1):
            if is_palindrome(string[i:]):
                # get the non-palindromic prefix of the string
                prefix = string[:i]
                # append the reverse prefix to the string
                return string + prefix[::-1]
        # if no palindromic suffix found, return the string with the first character repeated at the end
        return string + string[0]

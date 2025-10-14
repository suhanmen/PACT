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
        # if the string is already a palindrome, return it as-is
        return string
    else:
        # find the longest palindromic suffix of the string
        for i in range(len(string)-1, -1, -1):
            if is_palindrome(string[i:]):
                # if we find a palindromic suffix, construct the palindrome by
                # appending the reverse of the prefix before the suffix
                return string + string[:i][::-1]
        # if no palindromic suffix is found, construct the palindrome by
        # appending the reverse of the entire string
        return string + string[::-1]

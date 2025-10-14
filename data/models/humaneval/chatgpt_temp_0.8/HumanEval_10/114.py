def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    palindrome_suffix = ""
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            palindrome_suffix = string[i:]
            break
    return string + string[:len(string)-len(palindrome_suffix)][::-1] + palindrome_suffix

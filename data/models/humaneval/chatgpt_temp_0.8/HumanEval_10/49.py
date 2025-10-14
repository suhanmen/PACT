def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    # Check if the string is already a palindrome
    if is_palindrome(string):
        return string
    
    # Find the longest palindromic suffix
    suffix = ""
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            suffix = string[i:]
            break
    
    # Find the prefix that comes before the palindromic suffix
    prefix = ""
    for i in range(len(string)):
        if is_palindrome(string[:i+1]):
            prefix = string[:i+1]
    
    # Create the palindrome by appending the reverse of the prefix to the suffix
    palindrome = string + prefix[::-1] + suffix
    
    return palindrome

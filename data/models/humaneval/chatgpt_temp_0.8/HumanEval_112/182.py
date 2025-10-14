# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # remove all characters from s that are equal to any character in c
    s = "".join([char for char in s if char not in c])
    # check if the resulting string is a palindrome
    is_palindrome = s == s[::-1]
    # return the resulting string and the boolean value for is_palindrome
    return (s, is_palindrome)

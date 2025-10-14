# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # delete characters in s that are in c
    for char in c:
        s = s.replace(char, "")

    # check if result string is palindrome
    is_palindrome = s == s[::-1]

    return s, is_palindrome

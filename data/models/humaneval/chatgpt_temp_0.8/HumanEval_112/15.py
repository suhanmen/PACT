# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # delete all the characters in s that are equal to any character in c
    for char in c:
        s = s.replace(char, "")
    
    # check if the result string is palindrome
    is_palindrome = s == s[::-1]
    
    # return the result string and True/False for the check
    return (s, is_palindrome)

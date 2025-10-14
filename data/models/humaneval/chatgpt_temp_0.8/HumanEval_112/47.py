# CANNOT PARSE CODE SNIPPET
python
def reverse_delete(s, c):
    # delete all characters in s that are equal to any character in c
    for char in c:
        s = s.replace(char, '')
    
    # check if the result string is a palindrome
    is_palindrome = s == s[::-1]
    
    return (s, is_palindrome)

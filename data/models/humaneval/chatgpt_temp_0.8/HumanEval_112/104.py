# CANNOT PARSE CODE SNIPPET
python
def reverse_delete(s, c):
    # delete all characters in s that appear in c
    result = ''.join(char for char in s if char not in c)
    
    # check if the result string is palindrome
    is_palindrome = result == result[::-1]
    
    # return the result string and boolean value indicating palindrome or not
    return (result, is_palindrome)

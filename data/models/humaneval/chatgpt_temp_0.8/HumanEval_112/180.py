# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # Delete all characters in s that are equal to any character in c
    result_string = ''.join([char for char in s if char not in c])
  
    # Check if the resulting string is a palindrome
    is_palindrome = result_string == result_string[::-1]

    # Return the result string and whether it is a palindrome or not
    return (result_string, is_palindrome)

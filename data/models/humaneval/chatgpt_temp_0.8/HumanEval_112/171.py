# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    # Delete characters in c from s
    filtered_s = "".join([char for char in s if char not in c])
    # Check if the resulting string is palindrome
    is_palindrome = filtered_s == filtered_s[::-1]
    # Return the result as a tuple
    return (filtered_s, is_palindrome)

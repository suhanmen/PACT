# CANNOT PARSE
def reverse_delete(s, c):
    # Delete characters in s that are equal to any character in c
    result = ''.join([char for char in s if char not in c])

    # Check if the result string is a palindrome
    is_palindrome = result == result[::-1]

    # Return the result string and the palindrome check
    return (result, is_palindrome)

# Test cases
print(reverse_delete("abcde", "ae"))  # ('bcd', False)
print(reverse_delete("abcdef", "b"))  # ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))  # ('cdedc', True)
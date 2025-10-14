# CANNOT PARSE CODE SNIPPET
def reverse_delete(s, c):
    filtered_s = "".join([char for char in s if char not in c])
    is_palindrome = filtered_s == filtered_s[::-1]
    return (filtered_s, is_palindrome)

def reverse_delete(s,c):
    result = ""
    for char in s:
        if char not in c:
            result += char
    palindrome_check = result == result[::-1]
    return (result, palindrome_check)

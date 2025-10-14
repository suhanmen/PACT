def reverse_delete(s,c):
    # delete all characters in s that are equal to any character in c
    temp = ''
    for letter in s:
        if letter not in c:
            temp += letter
    # check if temp is a palindrome
    is_palindrome = temp == temp[::-1]
    return (temp, is_palindrome)

"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""



def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    string_list = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if string_list[i] in vowels:
            while string_list[j] not in vowels and i < j:
                j -= 1
            string_list[i], string_list[j] = string_list[j], string_list[i]
            j -= 1
        i += 1
    return ''.join(string_list)

# Example usage:
# reversed_string = reverse_vowels("Python")
# print(reversed_string)  # Output: Python

assert reverse_vowels("Python") == "Python"

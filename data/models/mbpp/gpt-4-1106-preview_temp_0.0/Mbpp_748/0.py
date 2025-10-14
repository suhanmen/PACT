"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""



def capital_words_spaces(s):
    result = ''
    for i, char in enumerate(s):
        if char.isupper() and i != 0:
            result += ' ' + char
        else:
            result += char
    return result

assert capital_words_spaces("Python") == 'Python'
assert capital_words_spaces("JavaC#Python") == 'Java C# Python'
assert capital_words_spaces("SplitCamelCase") == 'Split Camel Case'

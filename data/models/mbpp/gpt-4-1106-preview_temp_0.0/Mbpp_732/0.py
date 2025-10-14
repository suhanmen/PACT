"""
Write a function to replace all occurrences of spaces, commas, or dots with a colon.
assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
"""



def replace_specialchar(input_string):
    special_chars = [' ', ',', '.']
    for char in special_chars:
        input_string = input_string.replace(char, ':')
    return input_string

assert replace_specialchar('Python language, Programming language.') == 'Python:language::Programming:language:'

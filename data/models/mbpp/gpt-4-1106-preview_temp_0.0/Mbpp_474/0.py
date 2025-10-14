"""
Write a function to replace characters in a string.
assert replace_char("polygon",'y','l')==("pollgon")
"""



def replace_char(input_string, old_char, new_char):
    return input_string.replace(old_char, new_char)

assert replace_char("polygon", 'y', 'l') == ("pollgon")

"""
Write a function to remove all whitespaces from a string.
assert remove_all_spaces('python  program')==('pythonprogram')
"""



def remove_all_spaces(input_string):
    return input_string.replace(' ', '')

assert remove_all_spaces('python  program') == 'pythonprogram'

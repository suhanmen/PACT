"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""



def move_num(s):
    letters = ''.join([c for c in s if not c.isdigit()])
    numbers = ''.join([c for c in s if c.isdigit()])
    return letters + numbers

assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'

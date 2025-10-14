"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""



def extract_rear(tup):
    return [word[-1] for word in tup]

assert extract_rear(('Mers', 'for', 'Vers')) == ['s', 'r', 's']

"""
Write a function to sort a dictionary by value.
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""


import operator

def sort_counter(counter):
    return sorted(counter.items(), key=operator.itemgetter(1), reverse=True)

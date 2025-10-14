"""
Write a function to create a list of N empty dictionaries.
assert empty_list(5)==[{},{},{},{},{}]
"""


def empty_list(N):
    return [{} for _ in range(N)]

assert empty_list(5) == [{},{},{},{},{}]

"""
Write a function to get the frequency of all the elements in a list, returned as a dictionary.
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
"""

def freq_count(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

# Example usage:
# assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]) == {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}
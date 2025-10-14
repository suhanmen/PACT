"""
Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""


import collections

def count_reverse_pairs(str_list):
    # Create a counter for all strings in the list
    str_counter = collections.Counter(str_list)
    # Initialize count of pairs
    pair_count = 0

    # Iterate over the list
    for s in str_list:
        # Check if the reverse of the string is present in the counter
        if str_counter[s[::-1]] > 0:
            # Increment the count
            pair_count += 1
            # Decrement the count of the reverse string to avoid double counting
            str_counter[s[::-1]] -= 1

    # Since each pair is counted twice, divide the result by 2
    return pair_count // 2

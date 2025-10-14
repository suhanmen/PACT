"""
Write a function to extract the number of unique tuples in the given list.
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
"""



def extract_freq(tuples_list):
    # Use a set to store unique tuples, as sets do not allow duplicates
    unique_tuples = set()

    for tup in tuples_list:
        # Add the tuple to the set. If it's already there, nothing changes.
        unique_tuples.add(tup)

    # The number of unique tuples is the size of the set
    return len(unique_tuples)

# Test the function
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]) == 3

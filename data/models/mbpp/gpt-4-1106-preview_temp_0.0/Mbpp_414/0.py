"""
Write a python function to check whether any value in a sequence exists in a sequence or not.
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
"""



def overlapping(seq1, seq2):
    return any(element in seq2 for element in seq1)

# Example usage
# assert overlapping([1,2,3,4,5],[6,7,8,9]) == False

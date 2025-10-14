"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""



def find_sum(lst):
    # Create a dictionary to store the frequency of each element
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1

    # Calculate the sum of non-repeated elements
    sum_non_repeated = sum(num for num, count in freq.items() if count == 1)
    return sum_non_repeated

# Example usage
# assert find_sum([1,2,3,1,1,4,5,6]) == 21

"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""



def find_tuples(tuple_list, k):
    # Function to check if all elements in a tuple are divisible by k
    def is_divisible(t):
        return all(x % k == 0 for x in t)

    # Use a list comprehension to filter out tuples where all elements are divisible by k
    return [t for t in tuple_list if is_divisible(t)]

# Example usage
# assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]

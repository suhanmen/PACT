"""
Write a function to append the given list to the given tuples.
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
"""



def add_lists(lst, tpl):
    return tpl + tuple(lst)


# Example usage
# result = add_lists([5, 6, 7], (9, 10))
# print(result)  # Output should be (9, 10, 5, 6, 7)

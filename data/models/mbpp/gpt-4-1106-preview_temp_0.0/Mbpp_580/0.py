"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""



def extract_even(mixed_tuple):
    def is_even(num):
        return num % 2 == 0

    def remove_uneven(tpl):
        if isinstance(tpl, int):
            return tpl if is_even(tpl) else None
        else:
            cleaned = tuple(remove_uneven(item) for item in tpl if remove_uneven(item) is not None)
            return cleaned

    return remove_uneven(mixed_tuple)


# Example usage:
# assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)

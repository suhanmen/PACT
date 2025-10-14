"""
Write a function to convert all possible convertible elements in a list of lists to floats.
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
"""



def list_to_float(list_of_lists):
    def to_float(element):
        try:
            return float(element)
        except ValueError:
            return element

    return [tuple(to_float(item) for item in inner_list) for inner_list in list_of_lists]

# Example usage
# assert list_to_float([("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]

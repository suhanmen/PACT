def sort_even(l: list):
    even_list = sorted(l[::2])
    result = [None] * len(l)
    result[::2] = even_list
    result[1::2] = l[1::2]
    return result

def sorted_list_sum(lst):
    """
    Accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order.

    Args:
        lst (list): A list of strings.
        
    Returns:
        list: A list of strings in sorted order.
    """
    even_len_words = [word for word in lst if len(word) % 2 == 0]
    sorted_words = sorted(even_len_words, key=lambda x: (len(x), x))
    return sorted_words

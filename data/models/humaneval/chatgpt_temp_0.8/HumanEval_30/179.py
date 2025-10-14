def get_positive(l: list):
    """Return only positive numbers in the list."""
    pos_list = []
    for num in l:
        if num > 0:
            pos_list.append(num)
    return pos_list

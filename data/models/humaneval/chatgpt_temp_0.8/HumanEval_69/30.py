def search(lst):
    max_val = -1
    for val in set(lst):
        freq = lst.count(val)
        if val > freq and freq > max_val:
            max_val = freq
    return max_val if max_val > -1 else -1

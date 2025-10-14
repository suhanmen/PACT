def total_match(lst1, lst2):
    total_chars_1 = sum(len(word) for word in lst1)
    total_chars_2 = sum(len(word) for word in lst2)

    if total_chars_1 < total_chars_2:
        return lst1
    else:
        return lst2 if total_chars_2 < total_chars_1 else lst1

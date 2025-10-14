def total_match(lst1, lst2):
    total_chars_1 = sum(len(string) for string in lst1)
    total_chars_2 = sum(len(string) for string in lst2)
    if total_chars_1 < total_chars_2:
        return lst1
    elif total_chars_2 < total_chars_1:
        return lst2
    else:
        return lst1

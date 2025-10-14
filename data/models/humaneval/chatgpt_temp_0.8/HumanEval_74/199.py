def total_match(lst1, lst2):
    char_count_1 = sum(len(s) for s in lst1)
    char_count_2 = sum(len(s) for s in lst2)
    if char_count_1 < char_count_2:
        return lst1
    elif char_count_2 < char_count_1:
        return lst2
    else:
        return lst1

def total_match(lst1, lst2):
    total_len1 = sum(len(s) for s in lst1)
    total_len2 = sum(len(s) for s in lst2)
    if total_len1 < total_len2:
        return lst1
    elif total_len1 > total_len2:
        return lst2
    else:
        return lst1

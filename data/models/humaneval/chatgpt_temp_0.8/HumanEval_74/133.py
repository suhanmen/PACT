def total_match(lst1, lst2):
    len1 = sum(len(s) for s in lst1)
    len2 = sum(len(s) for s in lst2)

    if len1 < len2:
        return lst1
    elif len2 < len1:
        return lst2
    else:
        return lst1

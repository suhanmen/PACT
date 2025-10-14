def total_match(lst1, lst2):
    total_chars1 = sum(len(s) for s in lst1)
    total_chars2 = sum(len(s) for s in lst2)

    if total_chars1 < total_chars2:
        return lst1
    else:
        return lst2 if total_chars2 < total_chars1 else lst1

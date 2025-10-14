def total_match(lst1, lst2):
    lst1_chars = sum(len(s) for s in lst1)
    lst2_chars = sum(len(s) for s in lst2)
    if lst1_chars < lst2_chars:
        return lst1
    else:
        return lst2 if lst2_chars < lst1_chars else lst1

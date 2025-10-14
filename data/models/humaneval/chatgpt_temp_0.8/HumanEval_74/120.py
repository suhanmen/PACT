def total_match(lst1, lst2):
    total_chars_1 = sum(len(s) for s in lst1)
    total_chars_2 = sum(len(s) for s in lst2)
    
    if total_chars_1 == total_chars_2:
        return lst1
    
    return lst1 if total_chars_1 < total_chars_2 else lst2

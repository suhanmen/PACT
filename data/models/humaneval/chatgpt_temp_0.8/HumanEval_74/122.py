def total_match(lst1, lst2):
    len_lst1 = sum(len(s) for s in lst1)
    len_lst2 = sum(len(s) for s in lst2)
    
    if len_lst1 == len_lst2:
        return lst1
    
    return lst1 if len_lst1 < len_lst2 else lst2

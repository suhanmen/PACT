def total_match(lst1, lst2):
    total_len_lst1 = sum(map(len, lst1))
    total_len_lst2 = sum(map(len, lst2))
    
    if total_len_lst1 < total_len_lst2:
        return lst1
    elif total_len_lst1 > total_len_lst2:
        return lst2
    else:
        return lst1

def total_match(lst1, lst2):
    total_chars_lst1 = sum([len(s) for s in lst1]) # find total chars in lst1
    total_chars_lst2 = sum([len(s) for s in lst2]) # find total chars in lst2

    if total_chars_lst1 < total_chars_lst2: # if lst1 has less chars than lst2
        return lst1
    else:
        return lst2 # otherwise return lst2

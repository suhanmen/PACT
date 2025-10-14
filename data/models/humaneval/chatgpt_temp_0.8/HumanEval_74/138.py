def total_match(lst1, lst2):
    total_chars_lst1 = sum(len(string) for string in lst1)
    total_chars_lst2 = sum(len(string) for string in lst2)

    if total_chars_lst1 < total_chars_lst2:
        return lst1
    else:
        return lst2 if total_chars_lst1 > total_chars_lst2 else lst1

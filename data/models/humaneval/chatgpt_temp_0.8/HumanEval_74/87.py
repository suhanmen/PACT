def total_match(lst1, lst2):
    chars_in_lst1 = sum(len(word) for word in lst1)
    chars_in_lst2 = sum(len(word) for word in lst2)

    if chars_in_lst1 < chars_in_lst2:
        return lst1
    elif chars_in_lst2 < chars_in_lst1:
        return lst2
    else:
        return lst1

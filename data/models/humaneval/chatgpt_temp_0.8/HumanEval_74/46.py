def total_match(lst1, lst2):
    chars1 = sum(len(word) for word in lst1)
    chars2 = sum(len(word) for word in lst2)

    if chars1 > chars2:
        return lst2
    elif chars1 < chars2:
        return lst1
    else:
        return lst1

def total_match(lst1, lst2):
    chars1 = sum(len(word) for word in lst1)
    chars2 = sum(len(word) for word in lst2)

    if chars1 < chars2:
        return lst1
    elif chars2 < chars1:
        return lst2
    else:
        return lst1

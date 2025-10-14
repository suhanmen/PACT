def total_match(lst1, lst2):
    total1 = sum(len(str) for str in lst1)
    total2 = sum(len(str) for str in lst2)
    if total1 < total2:
        return lst1
    else:
        return lst2 if total1 > total2 else lst1

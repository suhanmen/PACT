def total_match(lst1, lst2):
    total1 = sum(len(string) for string in lst1)
    total2 = sum(len(string) for string in lst2)
    
    if total1 < total2:
        return lst1
    elif total2 < total1:
        return lst2
    else:
        return lst1

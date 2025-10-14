def total_match(lst1, lst2):
    total_1 = sum(len(s) for s in lst1)
    total_2 = sum(len(s) for s in lst2)
  
    if total_1 < total_2:
        return lst1
    elif total_1 == total_2:
        return lst1
    else:
        return lst2

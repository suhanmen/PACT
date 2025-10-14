def total_match(lst1, lst2):
    sum1 = sum(len(i) for i in lst1)
    sum2 = sum(len(i) for i in lst2)

    if sum1 < sum2:
        return lst1
    else:
        return lst2 if sum2 < sum1 else lst1

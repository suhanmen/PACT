def exchange(lst1, lst2):
    count_odd = sum([(x % 2) for x in lst1])
    if count_odd > len(lst2):
        return "NO"
    else:
        return "YES"

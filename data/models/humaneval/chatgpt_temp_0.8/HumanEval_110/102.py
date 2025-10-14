def exchange(lst1, lst2):
    even_lst1 = [x for x in lst1 if x % 2 == 0]
    count_odd_lst2 = sum([1 for x in lst2 if x % 2 != 0])
    if count_odd_lst2 > len(even_lst1):
        return "NO"
    else:
        return "YES"

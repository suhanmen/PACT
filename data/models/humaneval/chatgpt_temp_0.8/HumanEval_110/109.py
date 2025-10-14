def exchange(lst1, lst2):
    even = [x for x in lst1 if x % 2 == 0]
    odd = [x for x in lst1 if x % 2 != 0]
    if len(odd) > len(lst2):
        return "NO"
    else:
        for x in odd:
            if lst2.count(x % 2) < odd.count(x):
                return "NO"
        return "YES"

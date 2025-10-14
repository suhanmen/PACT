def exchange(lst1, lst2):
    if sum([1 for num in lst1 if num % 2 != 0]) > len(lst2):
        return "NO"
    else:
        return "YES"

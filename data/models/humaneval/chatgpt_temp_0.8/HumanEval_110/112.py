def exchange(lst1, lst2):
    lst1_even = [num for num in lst1 if num % 2 == 0]
    lst2_even = [num for num in lst2 if num % 2 == 0]
    if len(lst1_even) == len(lst1):
        return "YES"
    elif len(lst2_even) == len(lst2):
        return "NO"
    else:
        return "YES"

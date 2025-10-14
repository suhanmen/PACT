def exchange(lst1, lst2):
    even_lst1 = [x for x in lst1 if x % 2 == 0]  # get all the even numbers from lst1
    odd_lst2 = [x for x in lst2 if x % 2 != 0]   # get all the odd numbers from lst2
    if len(even_lst1) == len(lst1):   # if lst1 is already all even, return "YES"
        return "YES"
    if len(even_lst1) > len(lst1) // 2:   # if more than half of lst1 is even, return "YES"
        return "YES"
    if len(even_lst1) + len(odd_lst2) < len(lst1):   # if there are not enough numbers to exchange, return "NO"
        return "NO"
    return "YES"

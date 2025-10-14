def exchange(lst1, lst2):
    even_lst1 = [num for num in lst1 if num % 2 == 0]
    odd_lst1 = [num for num in lst1 if num % 2 != 0]
    odd_lst2 = [num for num in lst2 if num % 2 != 0]
    if len(odd_lst1) > len(odd_lst2):
        return "NO"
    else:
        return "YES"

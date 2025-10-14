def exchange(lst1, lst2):
    even_lst1 = [num for num in lst1 if num % 2 == 0] # create a new list with only even numbers from lst1
    odd_lst2 = [num for num in lst2 if num % 2 == 1] # create a new list with only odd numbers from lst2
    if len(even_lst1) == len(lst1): # if lst1 already contains only even numbers, return "YES"
        return "YES"
    elif len(even_lst1) + len(odd_lst2) == len(lst1): # if there are enough even and odd numbers to make lst1 all even, return "YES"
        return "YES"
    else:
        return "NO" # otherwise, it is not possible to make lst1 all even, so return "NO"

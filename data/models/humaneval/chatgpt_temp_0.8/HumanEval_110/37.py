def exchange(lst1, lst2):
    even_lst1 = [num for num in lst1 if num % 2 == 0]  # create a list of even numbers from lst1
    odd_lst2 = [num for num in lst2 if num % 2 == 1]  # create a list of odd numbers from lst2
    if len(even_lst1) == len(lst1):  # if lst1 already consists of only even numbers
        return "YES"
    elif len(even_lst1) + len(odd_lst2) == len(lst1):  # if lst1 and lst2 together have all even and odd numbers respectively
        return "YES"
    else:
        return "NO"

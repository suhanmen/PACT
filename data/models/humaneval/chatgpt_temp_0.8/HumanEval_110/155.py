def exchange(lst1, lst2):
    even_lst1 = [num for num in lst1 if num % 2 == 0] # Get all even numbers from lst1
    odd_lst2 = [num for num in lst2 if num % 2 != 0] # Get all odd numbers from lst2

    if len(even_lst1) == len(lst1): # If lst1 already contains only even numbers
        return "YES"
    elif len(even_lst1) + len(odd_lst2) == len(lst1): # If it's possible to exchange elements to make lst1 all even
        return "YES"
    else:
        return "NO"

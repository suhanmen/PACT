def exchange(lst1, lst2):
    even_lst1 = [num for num in lst1 if num % 2 == 0] # create a list with only even numbers from lst1
    odd_lst2 = [num for num in lst2 if num % 2 == 1] # create a list with only odd numbers from lst2
    
    if len(even_lst1) == len(lst1): # if lst1 already contains only even numbers
        return "YES"
    elif len(even_lst1) == 0 or len(odd_lst2) == 0: # if lst1 contains no even numbers or lst2 contains no odd numbers
        return "NO"
    else:
        return "YES" # otherwise, an exchange is possible

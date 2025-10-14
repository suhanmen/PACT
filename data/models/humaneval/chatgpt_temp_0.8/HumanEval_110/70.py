def exchange(lst1, lst2):
    even_lst1 = [num for num in lst1 if num % 2 == 0] # get even numbers from lst1
    odd_lst2 = [num for num in lst2 if num % 2 != 0] # get odd numbers from lst2
    
    # if there are not enough even numbers in lst1 to cover all odd numbers in lst2, return "NO"
    if len(even_lst1) < len(odd_lst2):
        return "NO"
    
    # otherwise, return "YES"
    return "YES"

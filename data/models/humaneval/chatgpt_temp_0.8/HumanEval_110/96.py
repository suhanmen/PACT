def exchange(lst1, lst2):
    # check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # find the indices of odd numbers in lst1
    odd_indices = [i for i, num in enumerate(lst1) if num % 2 != 0]
    
    # find the indices of even numbers in lst2
    even_indices = [i for i, num in enumerate(lst2) if num % 2 == 0]
    
    # check if there are enough even numbers in lst2 to replace the odd numbers in lst1
    if len(even_indices) >= len(odd_indices):
        return "YES"
    else:
        return "NO"

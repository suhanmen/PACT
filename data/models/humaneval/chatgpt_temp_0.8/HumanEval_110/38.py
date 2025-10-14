def exchange(lst1, lst2):
    # First, check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # If not, find the indices of the odd numbers in lst1
    odd_indices = [i for i, num in enumerate(lst1) if num % 2 != 0]
    
    # Check if there are enough even numbers in lst2 to exchange with odd numbers in lst1
    even_count = sum(1 for num in lst2 if num % 2 == 0)
    if even_count < len(odd_indices):
        return "NO"
    
    # If there are enough even numbers, swap them with odd numbers in lst1
    for i in odd_indices:
        for j, num in enumerate(lst2):
            if num % 2 == 0:
                lst1[i], lst2[j] = lst2[j], lst1[i]
                break
    
    # Check if all numbers in lst1 are now even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"

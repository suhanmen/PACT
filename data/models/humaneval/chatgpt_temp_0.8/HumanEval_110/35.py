def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the indices of odd numbers in lst1
    odd_indices = [i for i, num in enumerate(lst1) if num % 2 == 1]
    
    # Find the indices of even numbers in lst2
    even_indices = [i for i, num in enumerate(lst2) if num % 2 == 0]
    
    # If there are no odd numbers in lst1 or no even numbers in lst2, return "NO"
    if not odd_indices or not even_indices:
        return "NO"
    
    # Exchange the odd numbers in lst1 with the even numbers in lst2
    for i in odd_indices:
        for j in even_indices:
            lst1[i], lst2[j] = lst2[j], lst1[i]
            # Check if lst1 now contains only even numbers
            if all(num % 2 == 0 for num in lst1):
                return "YES"
    
    # If all possible exchanges have been tried and lst1 still contains odd numbers, return "NO"
    return "NO"

def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the indices of odd numbers in lst1
    odd_indices = [i for i, num in enumerate(lst1) if num % 2 != 0]
    
    # Find the indices of even numbers in lst2
    even_indices = [i for i, num in enumerate(lst2) if num % 2 == 0]
    
    # If there are no even numbers in lst2, it is impossible to make lst1 all even
    if not even_indices:
        return "NO"
    
    # Swap an odd number from lst1 with an even number from lst2
    lst1[odd_indices[0]], lst2[even_indices[0]] = lst2[even_indices[0]], lst1[odd_indices[0]]
    
    # Recursively call the function until lst1 is all even or all possible swaps have been tried
    return exchange(lst1, lst2)

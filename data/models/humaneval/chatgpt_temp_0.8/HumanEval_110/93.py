def exchange(lst1, lst2):
    # Check if lst1 already consists of all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the indexes of odd numbers in lst1
    odd_indexes = [i for i in range(len(lst1)) if lst1[i] % 2 != 0]
    
    # Find the indexes of even numbers in lst2
    even_indexes = [i for i in range(len(lst2)) if lst2[i] % 2 == 0]
    
    # If there are no odd numbers in lst1 or no even numbers in lst2, return "NO"
    if not odd_indexes or not even_indexes:
        return "NO"
    
    # Swap the odd number in lst1 with the even number in lst2
    lst1[odd_indexes[0]], lst2[even_indexes[0]] = lst2[even_indexes[0]], lst1[odd_indexes[0]]
    
    # Recursively call exchange function with swapped lists
    return exchange(lst1, lst2)

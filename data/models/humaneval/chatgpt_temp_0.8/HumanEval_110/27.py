def exchange(lst1, lst2):
    # Check if all numbers in lst1 are already even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find all even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # Sort lst1 in descending order
    lst1_sorted = sorted(lst1, reverse=True)
    
    # Try to replace odd numbers in lst1 with even numbers from lst2
    for i in range(len(lst1_sorted)):
        if lst1_sorted[i] % 2 != 0 and even_nums:
            lst1_sorted[i] = even_nums.pop()
    
    # Check if all numbers in lst1 are even after replacement
    if all(num % 2 == 0 for num in lst1_sorted):
        return "YES"
    else:
        return "NO"

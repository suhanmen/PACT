def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find indices of odd numbers in lst1
    odd_indices = [i for i, num in enumerate(lst1) if num % 2 != 0]
    
    # Find even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # If there are not enough even numbers in lst2, return "NO"
    if len(even_nums) < len(odd_indices):
        return "NO"
    
    # Exchange odd numbers in lst1 with even numbers in lst2
    for i in odd_indices:
        for j, num in enumerate(even_nums):
            if num % 2 != 0:
                continue
            lst1[i] = num
            even_nums[j] = float('inf')
            break
    
    # Check if all numbers in lst1 are even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    return "NO"

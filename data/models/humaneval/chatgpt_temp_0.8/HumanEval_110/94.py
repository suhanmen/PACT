def exchange(lst1, lst2):
    # Check if lst1 already consists of only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the odd numbers in lst1 and their indices
    odd_nums = [num for num in lst1 if num % 2 != 0]
    odd_indices = [i for i, num in enumerate(lst1) if num % 2 != 0]
    
    # Find the even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # If there are not enough even numbers in lst2 to replace the odd numbers in lst1,
    # return "NO"
    if len(even_nums) < len(odd_nums):
        return "NO"
    
    # Replace the odd numbers in lst1 with the even numbers from lst2
    for i, num in zip(odd_indices, even_nums):
        lst1[i] = num
    
    # Check if lst1 consists of only even numbers after the replacement
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"

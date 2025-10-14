def exchange(lst1, lst2):
    # Check if lst1 already has all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the odd numbers in lst1 and their indices
    odd_nums = [num for num in lst1 if num % 2 != 0]
    odd_indices = [i for i, num in enumerate(lst1) if num % 2 != 0]
    
    # Find the even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # If there are not enough even numbers in lst2 to replace the odd numbers in lst1, return "NO"
    if len(even_nums) < len(odd_nums):
        return "NO"
    
    # Sort the even numbers in descending order
    even_nums.sort(reverse=True)
    
    # Replace the odd numbers in lst1 with the even numbers from lst2
    for i, idx in enumerate(odd_indices):
        lst1[idx] = even_nums[i]
    
    # Check if lst1 now has all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"

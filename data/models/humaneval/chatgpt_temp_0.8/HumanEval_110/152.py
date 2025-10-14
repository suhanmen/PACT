def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Determine the odd numbers in lst1 and their positions
    odd_nums = [(num, idx) for idx, num in enumerate(lst1) if num % 2 != 0]
    
    # Iterate through lst2 to find even numbers and their positions
    even_nums = [(num, idx) for idx, num in enumerate(lst2) if num % 2 == 0]
    
    # Check if there are enough even numbers in lst2 to replace the odd numbers in lst1
    if len(even_nums) < len(odd_nums):
        return "NO"
    
    # Sort odd numbers in descending order and even numbers in ascending order
    odd_nums.sort(reverse=True)
    even_nums.sort()
    
    # Replace odd numbers in lst1 with even numbers from lst2
    for i in range(len(odd_nums)):
        lst1[odd_nums[i][1]] = even_nums[i][0]
    
    # Check if lst1 now contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    return "NO"

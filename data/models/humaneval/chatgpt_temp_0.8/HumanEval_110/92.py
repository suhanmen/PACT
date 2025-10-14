def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the odd numbers in lst1
    odd_nums = [num for num in lst1 if num % 2 != 0]
    
    # Find the even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # Check if there are enough even numbers in lst2 to replace the odd numbers in lst1
    if len(even_nums) < len(odd_nums):
        return "NO"
    
    # Sort the odd and even numbers in descending order
    odd_nums.sort(reverse=True)
    even_nums.sort(reverse=True)
    
    # Replace the odd numbers in lst1 with the even numbers from lst2
    for i in range(len(odd_nums)):
        lst1[lst1.index(odd_nums[i])] = even_nums[i]
    
    # Check if lst1 now contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    return "NO"
